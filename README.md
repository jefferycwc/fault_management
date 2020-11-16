1.redis
modify bind ip in /etc/redis/redis/conf
service redis-server restart
2.deploy master node as a service
cp master_node/MasterNode.service /etc/systemd/system