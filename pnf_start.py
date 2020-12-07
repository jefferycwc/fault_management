import paramiko
import time
from master_node.remote_connect import RemoteConnect

class PnfStart():
    def __init__(self):
        self.target_addr = '192.168.1.219'
        self.target_username = 'jeffery'
        self.target_password = 'jeffery71'
    
   
    def upf_start(self):
        cmds = ['cd /home/jeffery/all_in_one/src/upf/build\n','nohup ./bin/free5gc-upfd\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate UPF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate UPF')

    def nrf_start(self):
        cmds = ['nohup ./all_in_one/bin/nrf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate NRF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Start to activate NRF')

    def amf_start(self):
        cmds = ['nohup ./all_in_one/bin/amf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate AMF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate AMF')

    def smf_start(self):
        cmds = ['nohup ./all_in_one/bin/smf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate SMF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate SMF')

    def udr_start(self):
        cmds = ['nohup ./all_in_one/bin/udr\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate UDR')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate UDR')

    def pcf_start(self):
        cmds = ['nohup ./all_in_one/bin/pcf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate PCF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate PCF')

    def udm_start(self):
        cmds = ['nohup ./all_in_one/bin/udm\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate UDM')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate UDM')

    def nssf_start(self):
        cmds = ['nohup ./all_in_one/bin/nssf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate NSSF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate NSSF')

    def ausf_start(self):
        cmds = ['nohup ./all_in_one/bin/ausf\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        print('Start to activate AUSF')
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('Finish to activate AUSF')
        
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

  