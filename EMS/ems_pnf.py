import sys
import paramiko
import redis
import signal
import os
import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from master_node.remote_connect import RemoteConnect
from cmds_pnf import cmds_dict
from settings import *

class EMS():
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.connector = RemoteConnect(target_addr)
    def put_data(self,tunnel_name,flag):
        #r = redis.Redis(host='localhost', port=6379, db=0)
        self.r.set(tunnel_name,flag)

    def ResetUPF(self):
        cmds = cmds_dict['upf']
        cmds.insert(0,'kill -9 $(pidof ./bin/free5gc-upfd)\n')
        self.put_data('upf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('upf','off')

    def ResetAMF(self):
        cmds = cmds_dict['amf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/amf)\n')
        self.put_data('amf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('amf','off')

    def ResetSMF(self):
        cmds = cmds_dict['smf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/smf)\n')
        self.put_data('smf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('smf','off')

    def ResetUDR(self):
        cmds = cmds_dict['udr']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/udr)\n')
        self.put_data('udr','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('udr','off')

    def ResetPCF(self):
        cmds = cmds_dict['pcf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/pcf)\n')
        self.put_data('pcf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('pcf','off')

    def ResetUDM(self):
        cmds = cmds_dict['udm']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/udm)\n')
        self.put_data('udm','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('udm','off')

    def ResetNSSF(self):
        cmds = cmds_dict['nssf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/nssf)\n')
        self.put_data('nssf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('nssf','off')

    def ResetAUSF(self):
        cmds = cmds_dict['ausf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/ausf)\n')
        self.put_data('ausf','on')
        self.connector.ssh_direct(cmds,target_username,target_password)
        self.put_data('ausf','off')

    def HealPnf(self,pnf_name):
        print('EM detected {} fail'.format(pnf_name))
        print('EM start to heal {}'.format(pnf_name))
        if pnf_name=='nrf':
            self.ResetUPF()
            cmds = cmds_dict[pnf_name]
            self.connector.ssh_direct(cmds,target_username,target_password)
            self.ResetAMF()
            self.ResetSMF()
            self.resetUDR()
            self.ResetPCF()
            self.ResetUDM()
            self.ResetNSSF()
            self.ResetAUSF()    
        elif pnf_name=='upf':
            cmds = cmds_dict[pnf_name]
            self.connector.ssh_direct(cmds,target_username,target_password)
            self.ResetSMF()
        elif pnf_name=='smf':
            self.ResetUPF()
            cmds = cmds_dict[pnf_name]
            self.connector.ssh_direct(cmds,target_username,target_password)
        else:
            cmds = cmds_dict[pnf_name]
            self.connector.ssh_direct(cmds,target_username,target_password)
        print('EM finish heal {}'.format(pnf_name))

    def DetectPnf(self,pnf_name):
        #lock = 'on'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target_addr,22,username=target_username, password=target_password)
        if pnf_name == 'upf':
            cmd = 'ps -aux | grep ./bin/free5gc-upfd'
        else:
            cmd = 'ps -aux | grep ./all_in_one/bin/%s' % pnf_name
        #r = redis.Redis(host='localhost', port=6379, db=0)
        
        while(1):
            time.sleep(1)
            lock = self.r.get(pnf_name)
            if lock==None:
                continue
            else:
                lock = lock.decode()
            #print('lock:{}'.format(lock))
            if lock=='terminate':
                print('Terminate EM')
                sys.exit(1)
            if lock=='on':
                #print('match')
                continue
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.read().decode().split("\n")
            if len(out)!=4:
                self.HealPnf(pnf_name)

      

def kill_process():
    sys.exit(1)

if __name__ == '__main__':
    argv = sys.argv[1]
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        ems = EMS()
        ems.DetectPnf(argv)
    except KeyboardInterrupt:
        print("Terminate EM")
        kill_process()