import redis
import json
def publisher(instance_id,cause,name,channel_name):
    r = redis.Redis(host='192.168.1.219', port=6379, db=0)
    payload = {}
    payload['instance_id'] = instance_id
    payload['cause'] = cause
    payload['name'] = name 
    payload_values = json.dumps(payload)
    r.publish(
        channel_name,
        payload_values
    )