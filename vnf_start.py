import paramiko, base64,getpass,time
from master_node.ssh_jump import ssh_jump 
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
        cmds = ['cd /home/ubuntu/stage3/gtp5g\n','make\n','sudo make install\n','cd /home/ubuntu/stage3/src/upf\n','mkdir build\n','cd build\n','cmake ..\n','make -j`nproc`\n','sudo nohup ./bin/free5gc-upfd\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate UPF')
        ssh_jump(self.upf_instance_ip,cmds)
        print('Finish activate UPF')

    def nrf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/nrf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate NRF')
        ssh_jump(self.nrf_instance_ip,cmds)
        print('Finish activate NRF')

    def amf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/amf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate AMF')
        ssh_jump(self.amf_instance_ip,cmds)
        print('Finish activate AMF')

    def smf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/smf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate SMF')
        ssh_jump(self.smf_instance_ip,cmds)
        print('Finish activate SMF')

    def udr_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/udr\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate UDR')
        ssh_jump(self.udr_instance_ip,cmds)
        print('Finish activate UDR')

    def pcf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/pcf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate PCF')
        ssh_jump(self.pcf_instance_ip,cmds)
        print('Finish activate PCF')

    def udm_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/udm\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate UDM')
        ssh_jump(self.udm_instance_ip,cmds)
        print('Finish activate UDM')

    def nssf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/nssf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate NSSF')
        ssh_jump(self.nssf_instance_ip,cmds)
        print('Finish activate NSSF')

    def ausf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/ausf\n','sudo service VnfDetect restart\n','exit\n']
        print('Start to activate AUSF')
        ssh_jump(self.ausf_instance_ip,cmds)
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

    
    