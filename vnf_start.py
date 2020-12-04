import paramiko, base64,getpass,time
from master_node.remote_connect import RemoteConnect
class VNF_Start():
    def __init__(self):
        self.upf_instance_ip='172.24.4.111'
        self.nrf_instance_ip='172.24.4.101'
        self.amf_instance_ip='172.24.4.102'
        self.smf_instance_ip='172.24.4.103'
        self.udr_instance_ip='172.24.4.104'
        self.pcf_instance_ip='172.24.4.105'
        self.udm_instance_ip='172.24.4.106'
        self.nssf_instance_ip='172.24.4.107'
        self.ausf_instance_ip='172.24.4.108'
    
    def upf_start(self):
        print('Start to activate UPF')
        connector = RemoteConnect(self.upf_instance_ip)
        connector.transport_dir()
        cmds = ['chmod 777 stage3/src/upf/build/bin/free5gc-upfd\n','cd /home/ubuntu/stage3/gtp5g\n','make\n','sudo make install\n','cd /home/ubuntu/stage3/src/upf/build\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate UPF')

    def nrf_start(self):
        connector = RemoteConnect(self.nrf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/nrf\n','exit\n']
        print('Start to activate NRF')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate NRF')

    def amf_start(self):
        connector = RemoteConnect(self.amf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/amf\n','exit\n']
        print('Start to activate AMF')
        connector.ssh_jump(cmds)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate AMF')

    def smf_start(self):
        connector = RemoteConnect(self.smf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/smf\n','exit\n']
        print('Start to activate SMF')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate SMF')

    def udr_start(self):
        connector = RemoteConnect(self.udr_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/udr\n','exit\n']
        print('Start to activate UDR')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate UDR')

    def pcf_start(self):
        connector = RemoteConnect(self.pcf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/pcf\n','exit\n']
        print('Start to activate PCF')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate PCF')

    def udm_start(self):
        connector = RemoteConnect(self.udm_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/udm\n','exit\n']
        print('Start to activate UDM')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate UDM')

    def nssf_start(self):
        connector = RemoteConnect(self.nssf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/nssf\n','exit\n']
        print('Start to activate NSSF')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate NSSF')

    def ausf_start(self):
        connector = RemoteConnect(self.ausf_instance_ip)
        cmds = ['sudo nohup ./stage3/bin/ausf\n','exit\n']
        print('Start to activate AUSF')
        connector.ssh_jump(cmds)
        #time.sleep(1)
        cmds = ['sudo service VnfDetect start\n','exit\n']
        connector.ssh_jump(cmds)
        print('Finish activate AUSF')

    
if __name__ == '__main__':
    test=VNF_Start()
    test.upf_start()
    test.nrf_start()
    test.amf_start()
    test.smf_start()
    test.udr_start()
    test.pcf_start()
    test.udm_start()
    test.nssf_start()
    test.ausf_start()

    
    