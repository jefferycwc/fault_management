import paramiko, base64,getpass,time
from remote_connect import RemoteConnect
def reset(ip):
    if ip=='172.24.4.111':
        connector = RemoteConnect(ip)
        print('reset upf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./bin/free5gc-upfd)\n','cd /home/ubuntu/stage3/src/upf/lib/libgtp5gnl/tools\n','sudo ./gtp5g-link del upfgtp0\n','sudo rm /dev/mqueue/*\n','cd /home/ubuntu/stage3/src/upf/build\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.102':
        connector = RemoteConnect(ip)
        print('reset amf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/amf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/amf\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.103':
        connector = RemoteConnect(ip)
        print('reset smf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/smf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/smf\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.104':
        connector = RemoteConnect(ip)
        print('reset udr')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/udr)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udr\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.105':
        connector = RemoteConnect(ip)
        print('reset pcf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/pcf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/pcf\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.106':
        connector = RemoteConnect(ip)
        print('reset udm')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/udm)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udm\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.107':
        connector = RemoteConnect(ip)
        print('reset nssf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/nssf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/nssf\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)
    elif ip=='172.24.4.108':
        connector = RemoteConnect(ip)
        print('reset ausf')
        cmds = ['sudo service VnfDetect stop','sudo kill $(pidof ./stage3/bin/ausf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/ausf\n','exit\n']
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect restart\n','exit\n']
        connector.ssh_jump(cmds)

    #print('reset finish')
    return 