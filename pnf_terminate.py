import paramiko
import time
import redis
from master_node.remote_connect import RemoteConnect
from EMS.settings import *
class PnfTerminate():
    def __init__(self):
        pass
    
    def put_data(self,tunnel_name):
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set(tunnel_name,'break')

    def upf_terminate(self):
        cmds = ['kill -9 $(pidof ./bin/free5gc-upfd)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('upf')
        print('UPF terminated')

    def nrf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/nrf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('nrf')
        print('NRF terminated')

    def amf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/amf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('amf')
        print('AMF terminated')

    def smf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/smf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('smf')
        print('SMF terminated')

    def udr_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/udr)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('udr')
        print('UDR terminated')

    def pcf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/pcf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('pcf')
        print('PCF terminated')

    def udm_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/udm)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('udm')
        print('UDM terminated')

    def nssf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/nssf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('nssf')
        print('NSSF terminated')

    def ausf_terminate(self):
        cmds = ['kill -9 $(pidof ./all_in_one/bin/ausf)\n','exit\n']
        connector = RemoteConnect(target_addr)
        connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('ausf')
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

  