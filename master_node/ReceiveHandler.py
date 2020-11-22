from flask import Flask,render_template,request,jsonify
import requests
import os
import time
from oslo_log import log as logging
import logging
from HealVnfHandler import OpenStackAPI
from PublishHandler import publisher
from threading import Thread
import vnf_detect
LOG = logging.getLogger(__name__)
app = Flask(__name__)
app.config["DEBUG"] = True

pid_dict = {}
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
    thread = Thread(target=vnf_detect.start, kwargs={'vnf_name':vnf_name,'vnf_id':vnf_id})
    thread.start()
    return 'succesful'
    
@app.route('/healvnf', methods=['POST'])
def ReceiveHealVnfRequest():
    print('Receive HealVnfRequest from EM')
    data = request.get_json()
    vnf_id = data['vnf_id']
    instance_id = data['instance_id']
    cause = data['cause']
    name = data['name']
    def HealVnfProcessStart(vnf_id,instance_id,cause,name):
        time.sleep(2)
        app.logger.info('Start healing %s vnf',name)
        #LOG.info('Start healing %s vnf',name)
        #print('Start healing {} vnf',name)
        publisher(vnf_id,instance_id,cause,name,'notification1')
        new_item = OpenStackAPI()
        if cause == 'paused':
            result = new_item.unpause(instance_id,name)
        elif cause == 'suspended':
            result = new_item.resume(instance_id,name)
        elif cause == 'shutoff':
            result = new_item.reboot(instance_id,name)
        app.logger.info('Finish healing %s vnf',name)
        #LOG.info('Finish healing %s vnf',name)
        #print('Finish healing {} vnf',name)
        publisher(vnf_id,instance_id,cause,name,'notification2')
    thread = Thread(target=HealVnfProcessStart, kwargs={'vnf_id':vnf_id,'instance_id':instance_id,'cause':cause,'name':name})
    thread.start()
    print('Send HealVnfResponse to EM')
    return 'succesful'

if __name__ == "__main__":
    app.debug = True
    handler = logging.FileHandler('/var/log/tacker/tacker-monitor.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host='192.168.1.103',port=5010)
