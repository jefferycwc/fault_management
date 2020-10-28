import paramiko, base64,getpass,time
import ssh_jump from ssh_jump.py
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
    
    def upf_start():
        cmds = ['cd /home/ubuntu/stage3/gtp5g\n','sudo make install\n','cd /home/ubuntu/stage3/src/upf\n','mkdir build\n','cd build\n','cmake ..\n','make -j`nproc`\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
        ssh_jump(upf_instance_ip,cmds)

    def nrf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/nrf\n','exit\n']
        ssh_jump(nrf_instance_ip,cmds)

    def amf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/amf\n','exit\n']
        ssh_jump(amf_instance_ip,cmds)

    def smf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/smf\n','exit\n']
        ssh_jump(smf_instance_ip,cmds)

    def udr_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/udr\n','exit\n']
        ssh_jump(udr_instance_ip,cmds)

    def pcf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/pcf\n','exit\n']
        ssh_jump(pcf_instance_ip,cmds)

    def udm_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/udm\n','exit\n']
        ssh_jump(udm_instance_ip,cmds)

    def nssf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/nssf\n','exit\n']
        ssh_jump(udr_instance_ip,cmds)

    def ausf_start():
        cmds = ['cd stage3\n','sudo nohup ./bin/ausf\n','exit\n']
        ssh_jump(ausf_instance_ip,cmds)

    
if __name__ == '__main__':
    test=VNF_Start()
    
    