import redis

r = redis.Redis(host='192.168.1.219', port=6379, db=0)
r.publish(
    'pcf_channel',
    'shutoff',
)