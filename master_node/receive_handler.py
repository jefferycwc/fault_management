from flask import Flask,render_template,request,jsonify
import requests
import os
import time
import logging
from healvnf_handler import OpenStackAPI
from instance_detect import OpenStackAPI as OpenStack
from instance_detect import TackerAPI as Tacker
from publish_handler import publisher
from threading import Thread
import instance_detect
from remote_connect import RemoteConnect
LOG = logging.getLogger(__name__)
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/addmonitor', methods=['POST'])
def AddMonitor():
    data = request.get_json()
    vnf_id = data['id']
    description = data['description']
    #print('description: {}'.format(description))
    vnf_name = description.split(':')[1]
    #print('vnf name: {}'.format(vnf_name))
    #LOG.info('Start monitoring %s',vnf_name)
    app.logger.info('Start monitoring %s',vnf_name)
    thread = Thread(target=instance_detect.start, kwargs={'vnf_name':vnf_name,'vnf_id':vnf_id})
    thread.start()
    return 'succesful'

@app.route('/vnf_monitor', methods=['POST'])
def VnfMonitor():
    data = request.get_json()
    management_urls = data['management_urls']
    cmds = ['sudo service VnfDetect start\n','exit\n']
    def VnfMonitor_(cmds,management_urls):
        for ip in management_urls:
            connector = RemoteConnect(ip)
            connector.ssh_jump(cmds)
    thread = Thread(target=VnfMonitor_, kwargs={'cmds':cmds,'management_urls':management_urls})
    thread.start()
    #thread.join()
    return 'successful'

@app.route('/healvnf', methods=['POST'])
def ReceiveHealVnfRequest():
    #print('Receive HealVnfRequest from EM')
    data = request.get_json()
    vnf_id = data['vnf_id']
    instance_id = data['instance_id']
    cause = data['cause']
    name = data['name']
    cmds = data['cmds']
    ip = data['ip']
    #print(cmds)
    #print(ip)
    app.logger.info('VNFM healed %s vnf, cause was %s',name,cause)
    def HealVnfProcessStart(vnf_id,instance_id,cause,name,cmds,ip):
        time.sleep(2)
        publisher(vnf_id,instance_id,cause,name,'notification1')
        new_item = OpenStackAPI()
        if cause == 'paused':
            result = new_item.unpause(instance_id)
        elif cause == 'suspended':
            result = new_item.resume(instance_id,cause,name,cmds,ip)
        elif cause == 'shutoff':
            result = new_item.reboot(instance_id,cause,name,cmds,ip)
        elif cause == 'vnf stop running':
            result = new_item.restart(name,cmds,ip,cause)
        publisher(vnf_id,instance_id,cause,name,'notification2')
    thread = Thread(target=HealVnfProcessStart, kwargs={'vnf_id':vnf_id,'instance_id':instance_id,'cause':cause,'name':name,'cmds':cmds,'ip':ip})
    thread.start()
    #print('Send HealVnfResponse to EM')
    return 'succesful'

@app.route('/alarm', methods=['POST'])
def ReceiveVnfAlarm():
    data = request.get_json()
    vnf_name = data['vnf_name']
    app.logger.info('{} stop running'.format(vnf_name))
    openstack = OpenStack()
    tacker = Tacker()
    instance_id = openstack.get_instance_id(vnf_name)
    vnf_id = tacker.get_vnf_id(vnf_name)
    cause = 'vnf stop running'
    publisher(vnf_id,instance_id,cause,vnf_name,'report')
    return 'succesful'

if __name__ == "__main__":
    #app.debug = True
    handler = logging.FileHandler('/var/log/tacker/tacker.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host='192.168.1.103',port=5010)
