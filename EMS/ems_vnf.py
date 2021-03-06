import redis
import json
import signal
import os
import sys
from healvnf_request import SendHealVnfRequest
from cmds_vnf import cmds_dict,ip_dict
def subscriber(tunnel_name):
    r = redis.Redis(host='192.168.1.103', port=6379, db=0)
    sub = r.pubsub()
    #print(tunnel_name)
    sub.subscribe(tunnel_name)
    for message in sub.listen():
        if message['type'] == 'subscribe':
            if message['data'] == 1:
                print('EM subscribed to VNFM')
        elif message['type'] == 'message':
            #print(json.loads(message['data']))
            data = json.loads(message['data'])
            vnf_id =  data['vnf_id']
            instance_id = data['instance_id']
            cause = data['cause']
            name = data['name']
            type = data['type']
            if type=='report':
                #print('Receive vnf instance fault report : {name} {cause}'.format(name=name,cause=cause))
                print('Receive vnf instance fault report: ')
                print(data)
                cmds = cmds_dict[name]
                ip = ip_dict[name]
                SendHealVnfRequest(vnf_id,instance_id,cause,name,cmds,ip)
            elif type=='notification1':
                print('Got notification from VNFM, heal VNF ({}) process start'.format(name))
            elif type=='notification2':
                print('Got notification from VNFM, heal VNF ({})process finish'.format(name,cause))
def kill_process():
    sys.exit(1)

if __name__ == '__main__':
    argv = sys.argv[1]
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        subscriber(argv)
    except KeyboardInterrupt:
        print("Terminate EM")
        kill_process()
