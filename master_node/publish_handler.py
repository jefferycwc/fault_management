import redis
import json
def publisher(vnf_id,instance_id,cause,name,type):
    r = redis.Redis(host='192.168.1.103', port=6379, db=0)
    payload = {}
    payload['name'] = name
    payload['vnf_id'] = vnf_id
    payload['instance_id'] = instance_id
    payload['cause'] = cause
    payload['type'] = type
    payload_values = json.dumps(payload)
    #if type=='instance':
        #print('Send vnf instance fault report')
    r.publish(
        name,
        payload_values
    )
