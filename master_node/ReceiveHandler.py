from flask import Flask,render_template,request,jsonify
import requests
import os
import time
from oslo_log import log as logging
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
    LOG.debug('Start monitoring {}'.format(vnf_name))
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
        LOG.debug('Start healing {} vnf'.format(vnf_name))
        publisher(vnf_id,instance_id,cause,name,'notification1')
        new_item = OpenStackAPI()
        if cause == 'paused':
            result = new_item.unpause(instance_id,name)
        elif cause == 'suspended':
            result = new_item.resume(instance_id,name)
        elif cause == 'shutoff':
            result = new_item.reboot(instance_id,name)
        LOG.debug('Finish healing {} vnf'.format(vnf_name))
        publisher(vnf_id,instance_id,cause,name,'notification2')
    thread = Thread(target=HealVnfProcessStart, kwargs={'vnf_id':vnf_id,'instance_id':instance_id,'cause':cause,'name':name})
    thread.start()
    print('Send HealVnfResponse to EM')
    return 'succesful'

if __name__ == "__main__":
    app.run(host='192.168.1.103',port=5010)
