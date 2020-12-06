import paramiko
import time
from master_node.remote_connect import RemoteConnect

class PnfStart():
    def __init__(self):
        self.target_addr = '192.168.1.219'
        self.target_username = 'jeffery'
        self.target_password = 'jeffery71'
        self.cmds = ['sudo nohup ./all_in_one/src/upf/build/bin/free5gc-upfd\n','sudo nohup ./all_in_one/bin/nrf\n','sudo nohup ./all_in_one/bin/amf\n','sudo nohup ./all_in_one/bin/smf\n',
        'sudo nohup ./all_in_one/bin/udr\n','sudo nohup ./all_in_one/bin/pcf\n','sudo nohup ./all_in_one/bin/udm\n','sudo nohup ./all_in_one/bin/nssf\n','sudo nohup ./all_in_one/bin/auf\n','exit\n']
   
    def start(self):
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(self.cmds,self.target_username,self.target_password)
    
if __name__ == '__main__':
    test=PnfStart()
    test.start()

  