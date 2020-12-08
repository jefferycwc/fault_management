import paramiko
import time
import redis
from master_node.remote_connect import RemoteConnect
from EMS.settings import *
class PnfStart():
    def __init__(self):
        pass
    
    def publisher(self,tunnel_name):
        r = redis.Redis(host='localhost', port=6379, db=0)
        payload = {}
        payload['lock'] = 'off'
        payload_values = json.dumps(payload)
        r.publish(
            tunnel_name,
            payload_values
        )
   
    def upf_start(self):
        cmds = ['cd /home/jeffery/all_in_one/src/upf/build\n','nohup ./bin/free5gc-upfd\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate UPF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('upf')
        print('Finish to activate UPF')

    def nrf_start(self):
        cmds = ['nohup ./all_in_one/bin/nrf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate NRF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('nrf')
        print('Start to activate NRF')

    def amf_start(self):
        cmds = ['nohup ./all_in_one/bin/amf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate AMF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('amf')
        print('Finish to activate AMF')

    def smf_start(self):
        cmds = ['nohup ./all_in_one/bin/smf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate SMF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('smf')
        print('Finish to activate SMF')

    def udr_start(self):
        cmds = ['nohup ./all_in_one/bin/udr\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate UDR')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('udr')
        print('Finish to activate UDR')

    def pcf_start(self):
        cmds = ['nohup ./all_in_one/bin/pcf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate PCF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('pcf')
        print('Finish to activate PCF')

    def udm_start(self):
        cmds = ['nohup ./all_in_one/bin/udm\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate UDM')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('udm')
        print('Finish to activate UDM')

    def nssf_start(self):
        cmds = ['nohup ./all_in_one/bin/nssf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate NSSF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('nssf')
        print('Finish to activate NSSF')

    def ausf_start(self):
        cmds = ['nohup ./all_in_one/bin/ausf\n','exit\n']
        connector = RemoteConnect(target_addr)
        print('Start to activate AUSF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('ausf')
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

  