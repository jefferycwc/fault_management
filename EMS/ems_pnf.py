import sys
import paramiko
import redis
import signal
import os
import json
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from master_node.remote_connect import RemoteConnect
from cmds_pnf import cmds_dict
from settings import *

def HealPnf(pnf_name):
    print('EM detected {} fail'.format(pnf_name))
    connector = RemoteConnect(target_addr)
    print('EM start to heal {}'.format(pnf_name))
    if pnf_name=='nrf':
        cmds = cmds_dict['upf']
        cmds.insert(0,'kill -9 $(pidof ./bin/free5gc-upfd)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['amf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/amf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['smf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/smf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['udr']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/udr)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['pcf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/pcf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['udm']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/udm)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['nssf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/nssf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['ausf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/ausf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
    elif pnf_name=='upf':
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['smf']
        cmds.insert(0,'kill -9 $(pidof ./all_in_one/bin/smf)\n')
        connector.ssh_direct(cmds,target_username,target_password)
    else:
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
    print('EM finish heal {}'.format(pnf_name))

def DetectPnf(pnf_name):
    lock = 'on'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(target_addr,22,username=target_username, password=target_password)
    if pnf_name == 'upf':
        cmd = 'ps -aux | grep ./bin/free5gc-upfd'
    else:
        cmd = 'ps -aux | grep ./all_in_one/bin/%s' % pnf_name
    r = redis.Redis(host='localhost', port=6379, db=0)
    sub = r.pubsub()
    sub.subscribe(pnf_name)
    for message in sub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            lock = data['lock']
            print('lock: {}'.format(lock))
    
    while(1):
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.read().decode().split("\n")
        '''if len(out)==4:
            lock = False'''
        if len(out)!=4 and lock=='off':
            HealPnf(pnf_name)

      

def kill_process():
    sys.exit(1)

if __name__ == '__main__':
    argv = sys.argv[1]
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        DetectPnf(argv)
    except KeyboardInterrupt:
        print("Terminate EM")
        kill_process()