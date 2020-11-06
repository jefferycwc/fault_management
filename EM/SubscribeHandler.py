import redis
from HealVnfRequest import SendHealVnfRequest
r = redis.Redis(host='192.168.1.219', port=6379, db=0)
sub = r.pubsub()
sub.subscribe('pcf_channel')
for message in sub.listen():
    if message['type'] == 'subscribe':
        if message['data'] == 1:
            log.info('subscribed to: %s' % (message['channel']))
    elif message['type'] == 'message':   
        print(json.loads(message['data']))
    