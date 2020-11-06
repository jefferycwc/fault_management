import redis,json
from HealVnfRequest import SendHealVnfRequest
def subscriber(channel_name):
    r = redis.Redis(host='192.168.1.219', port=6379, db=0)
    sub = r.pubsub()
    sub.subscribe(channel_name)
    for message in sub.listen():
        if message['type'] == 'subscribe':
            if message['data'] == 1:
                print('subscribed to {}'.format(message['channel']))
        elif message['type'] == 'message':   
            #print(json.loads(message['data']))
            data = json.loads(message['data'])
            instance_id = data['instance_id']
            cause = data['cause']
            name = data['name']
            print('Got vnf instance error notification : {name} {cause}'.format(name=name,cause=cause))
            SendHealVnfReques(instance_id,cause,name)