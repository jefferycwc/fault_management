mongodb_list = ['sudo systemctl start mongod','exit\n']
upf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3/gtp5g\n','sudo make install\n','cd /home/ubuntu/stage3/src/upf/lib/libgtp5gnl/tools\n','sudo ./gtp5g-link del upfgtp0\n','sudo rm /dev/mqueue/*\n','cd /home/ubuntu/stage3/src/upf/build\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
nrf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/nrf & \n','exit\n']
amf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/amf & \n','exit\n']
smf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/smf & \n','exit\n']
udr_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udr & \n','exit\n']
pcf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/pcf & \n','exit\n']
udm_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udm & \n','exit\n']
nssf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/nssf & \n','exit\n']
ausf_list = ['service VnfDetect start\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/ausf & \n','exit\n']
cmds_dict = {'mongodb':mongodb_list,'upf':upf_list,'nrf':nrf_list,'amf':amf_list,'smf':smf_list,'udr':udr_list,'pcf':pcf_list,'udm':udm_list,'nssf':nssf_list,'ausf':ausf_list}
ip_dict = {'mongodb': '172.24.4.110', 'upf': '172.24.4.111', 'nrf': '172.24.4.101', 'amf': '172.24.4.102', 'smf': '172.24.4.103', 'udr': '172.24.4.104', 'pcf': '172.24.4.105', 'udm': '172.24.4.106', 'nssf': '172.24.4.107', 'ausf': '172.24.4.108'}
