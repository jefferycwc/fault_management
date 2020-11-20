from flask import Flask,render_template,request,jsonify
import requests
import os
import time
from HealVnfHandler import OpenStackAPI
from PublishHandler import publisher
from threading import Thread
#import multiprocessing
#import amf_detect
import vnf_detect
app = Flask(__name__)
app.config["DEBUG"] = True

pid_dict = {}
@app.route('/addmonitor', methods=['POST'])
def AddMonitor():
    data = request.get_json()
    vnf_id = data['id']
    description = data['description']
    print('description: {}'.format(description))
    vnf_name = description.split(':')[1]
    print('vnf name: {}'.format(vnf_name))
    thread = Thread(target=vnf_detect.start, kwargs={'vnf_name':vnf_name,'vnf_id':vnf_id})
    thread.start()
    '''if vnf_name == 'mongodb':
        mongodb_proc =  multiprocessing.Process(target=vnf_detect.start, kwargs={'vnf_name':vnf_name,'vnf_id':vnf_id})
        mongodb_proc.start()
    elif vnf_name == 'amf':
        amf_proc =  multiprocessing.Process(target=vnf_detect.start, kwargs={'vnf_name':vnf_name,'vnf_id':vnf_id})
        amf_proc.start()'''
    '''pid = os.fork()
    if pid == 0:
        vnf_detect.start(vnf_name,vnf_id)
    else:
        print('{} process pid: {}'.format(vnf_name,os.getppid()))
        pid_dict[vnf_name] = os.getppid()'''
    return 'succesful'
    
@app.route('/healvnf', methods=['POST'])
def ReceiveHealVnfRequest():
    print('Receive HealVnfRequest from EM')
    data = request.get_json()
    vnf_id = data['vnf_id']
    instnace_id = data['instance_id']
    cause = data['cause']
    name = data['name']
    #print('vnf instance id = {id} cause = {cause}'.format(id=id,cause=cause))
    #pid = os.fork()
    #if pid==0:
    def HealVnfProcessStart(instance_id,cause,name):
        #print('child id : {}'.format(os.getpid()))
        time.sleep(2)
        publisher(vnf_id,instance_id,cause,name,'notification1')
        new_item = OpenStackAPI()
        if cause == 'paused':
            result = new_item.unpause(id)
        elif cause == 'suspended':
            result = new_item.resume(id,name)
        elif cause == 'shutoff':
            result = new_item.reboot(id,name)
        publisher(vnf_id,instance_id,cause,name,'notification2')
        #os.kill(os.getpid())
    thread = Thread(target=HealVnfProcessStart, kwargs={'vnf_id':vnf_id,'instance_id':instance_id,'cause':cause,'name':name})
    thread.start()
    print('Send HealVnfResponse to EM')
    return 'succesful'

if __name__ == "__main__":
    app.run(host='192.168.1.103',port=5010)
