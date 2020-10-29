import paramiko, base64,getpass,time
from ssh_jump import ssh_jump 
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
        cmds = ['cd /home/ubuntu/stage3/src/upf\n','mkdir build\n','cd build\n','cmake ..\n','make -j`nproc`\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
        ssh_jump(self.upf_instance_ip,cmds)

    def nrf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/nrf\n','exit\n']
        ssh_jump(self.nrf_instance_ip,cmds)

    def amf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/amf\n','exit\n']
        ssh_jump(self.amf_instance_ip,cmds)

    def smf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/smf\n','exit\n']
        ssh_jump(self.smf_instance_ip,cmds)

    def udr_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/udr\n','exit\n']
        ssh_jump(self.udr_instance_ip,cmds)

    def pcf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/pcf\n','exit\n']
        ssh_jump(self.pcf_instance_ip,cmds)

    def udm_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/udm\n','exit\n']
        ssh_jump(self.udm_instance_ip,cmds)

    def nssf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/nssf\n','exit\n']
        ssh_jump(self.nssf_instance_ip,cmds)

    def ausf_start(self):
        cmds = ['cd stage3\n','sudo nohup ./bin/ausf\n','exit\n']
        ssh_jump(self.ausf_instance_ip,cmds)

    
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

    
    