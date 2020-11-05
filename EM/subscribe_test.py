import redis

r = redis.Redis(host='192.168.1.219', port=6379, db=0)
sub = r.pubsub()
sub.subscribe('my_redis_channel')
for message in sub.listen():
    print('Got message', message)
    if (
        isinstance(message.get('data'), bytes) and
        message['data'].decode() == 'GREETING'
    ):
        print('Hello')