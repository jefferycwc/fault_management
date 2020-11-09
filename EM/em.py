import redis
import json
import signal
import os
from HealVnfRequest import SendHealVnfRequest
def subscriber():
    r = redis.Redis(host='192.168.1.219', port=6379, db=0)
    sub = r.pubsub()
    sub.subscribe('error_report')
    #sub.psubscribe('__keyspace@0__:*')
    for message in sub.listen():
        if message['type'] == 'subscribe':
            if message['data'] == 1:
                print('EM subscribed to VNFM')
        elif message['type'] == 'message':
            #print(json.loads(message['data']))
            data = json.loads(message['data'])
            instance_id = data['instance_id']
            cause = data['cause']
            name = data['name']
            type = data['type']
            if type=='report':
                print('Receive vnf instance fault report : {name} {cause}'.format(name=name,cause=cause))
                SendHealVnfRequest(instance_id,cause,name)
            elif type=='notification1':
                print('Got notification from VNFM, heal VNF process start')
            elif type=='notification2':
                print('Got notification from VNFM, heal VNF process finish')
def kill_process():
   for line in os.popen("ps ax | grep em.py | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        #print(pid)
        os.kill(int(pid), signal.SIGKILL)

if __name__ == '__main__':
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        subscriber()
    except KeyboardInterrupt:
        print("Terminate EM")
        kill_process()
