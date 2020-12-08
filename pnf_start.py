import paramiko
import time
import redis
import json
from master_node.remote_connect import RemoteConnect
from EMS.settings import *
from cmds_pnf import cmds_dict
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
        cmds=cmds_dict['upf']
        connector = RemoteConnect(target_addr)
        print('Start to activate UPF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('upf')
        print('Finish to activate UPF')

    def nrf_start(self):
        cmds=cmds_dict['nrf']
        connector = RemoteConnect(target_addr)
        print('Start to activate NRF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('nrf')
        print('Start to activate NRF')

    def amf_start(self):
        cmds=cmds_dict['amf']
        connector = RemoteConnect(target_addr)
        print('Start to activate AMF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('amf')
        print('Finish to activate AMF')

    def smf_start(self):
        cmds=cmds_dict['smf']
        connector = RemoteConnect(target_addr)
        print('Start to activate SMF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('smf')
        print('Finish to activate SMF')

    def udr_start(self):
        cmds=cmds_dict['udr']
        connector = RemoteConnect(target_addr)
        print('Start to activate UDR')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('udr')
        print('Finish to activate UDR')

    def pcf_start(self):
        cmds=cmds_dict['pcf']
        connector = RemoteConnect(target_addr)
        print('Start to activate PCF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('pcf')
        print('Finish to activate PCF')

    def udm_start(self):
        cmds=cmds_dict['udm']
        connector = RemoteConnect(target_addr)
        print('Start to activate UDM')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('udm')
        print('Finish to activate UDM')

    def nssf_start(self):
        cmds=cmds_dict['nssf']
        connector = RemoteConnect(target_addr)
        print('Start to activate NSSF')
        connector.ssh_direct(cmds,target_username,target_password)
        self.publisher('nssf')
        print('Finish to activate NSSF')

    def ausf_start(self):
        cmds=cmds_dict['ausf']
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

  