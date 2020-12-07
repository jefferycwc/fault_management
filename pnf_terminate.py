import paramiko
import time
from master_node.remote_connect import RemoteConnect

class PnfTerminate():
    def __init__(self):
        self.target_addr = '192.168.1.219'
        self.target_username = 'jeffery'
        self.target_password = 'jeffery71'
    
   
    def upf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/free5gc-upfd)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('UPF terminated')

    def nrf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/nrf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('NRF terminated')

    def amf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/amf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('AMF terminated')

    def smf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/smf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('SMF terminated')

    def udr_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/udr)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('UDR terminated')

    def pcf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/pcf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('PCF terminated')

    def udm_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/udm)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('UDM terminated')

    def nssf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/nssf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('NSSF terminated')

    def ausf_terminate(self):
        cmds = ['sudo kill $(pidof ./bin/ausf)\n','exit\n']
        connector = RemoteConnect(self.target_addr)
        connector.ssh_direct(cmds,self.target_username,self.target_password)
        print('AUSF terminated')
        
if __name__ == '__main__':
    test=PnfTerminate()
    test.upf_terminate()
    test.nrf_terminate()
    test.amf_terminate()
    test.smf_terminate()
    test.udr_terminate()
    test.pcf_terminate()
    test.udm_terminate()
    test.nssf_terminate()
    test.ausf_terminate()

  