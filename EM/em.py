import redis
import json
import signal
import os
from HealVnfRequest import SendHealVnfRequest
def subscriber():
    r = redis.Redis(host='192.168.1.219', port=6379, db=0)
    sub = r.pubsub()
    sub.subscribe('error_report')
    for message in sub.listen():
        if message['type'] == 'subscribe':
            if message['data'] == 1:
                print('EM subscribed to Master Node')
        elif message['type'] == 'message':   
            #print(json.loads(message['data']))
            data = json.loads(message['data'])
            instance_id = data['instance_id']
            cause = data['cause']
            name = data['name']
            print('Got vnf instance error notification : {name} {cause}'.format(name=name,cause=cause))
            SendHealVnfRequest(instance_id,cause,name)
def kill_process():
   for line in os.popen("ps ax | grep em.py | grep -v grep"):
        fields = line.split() 
        pid = fields[0]
        print(pid)
        os.kill(int(pid), signal.SIGKILL)     

if __name__ == '__main__':
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        subscriber()
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        kill_process()