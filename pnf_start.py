import paramiko
import time
from master_node.remote_connect import RemoteConnect

class PnfStart():
    def __init__(self):
        self.target_addr = '192.168.1.219'
        self.target_username = 'jeffery'
        self.target_password = 'jeffery71'
    
   
    def upf_start(self):
        cmds = ['nohup ./all_in_one/src/upf/build/bin/free5gc-upfd\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def nrf_start(self):
        cmds = ['nohup ./all_in_one/bin/nrf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def amf_start(self):
        cmds = ['nohup ./all_in_one/bin/amf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def smf_start(self):
        cmds = ['nohup ./all_in_one/bin/smf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
    
    def udr_start(self):
        cmds = ['nohup ./all_in_one/bin/udr\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def pcf_start(self):
        cmds = ['nohup ./all_in_one/bin/pcf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def udm_start(self):
        cmds = ['nohup ./all_in_one/bin/udm\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def nssf_start(self):
        cmds = ['nohup ./all_in_one/bin/nssf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)

    def ausf_start(self):
        cmds = ['nohup ./all_in_one/bin/ausf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
if __name__ == '__main__':
    test=PnfStart()
    test.upf_start()
    test.nrf_start()
    test.amf_start()
    test.smf_start()
    test.udr_start()
    test.pcf_start()
    test.udm_start()
    test.nssf_start()
    test.ausf_start()

  