import sys
import paramiko
import signal
from master_node.remote_connect import RemoteConnect
from cmds_vnf import cmds_dict
from settings import *

def HealPnf(pnf_name):
    print('EM detected {} fail'.fromat(pnf_name))
    connector = RemoteConnect(target_addr)
    print('EM start to heal {}'.format(pnf_name))
    if pnf_name=='nrf':
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['amf']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['smf']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['udr']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['pcf']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['udm']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['nssf']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['ausf']
        connector.ssh_direct(cmds,target_username,target_password)
    elif pnf_name=='upf':
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict['smf']
        connector.ssh_direct(cmds,target_username,target_password)
    elif pnf_name=='smf':
        cmds = cmds_dict['upf']
        connector.ssh_direct(cmds,target_username,target_password)
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
    else:
        cmds = cmds_dict[pnf_name]
        connector.ssh_direct(cmds,target_username,target_password)
    print('EM finish heal {}'.format(pnf_name))

def DetectPnf(pnf_name):
    lock = True
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(target_addr,22,username=target_username, password=target_password)
    if pnf_name == 'upf':
        cmd = 'ps -aux | grep ./bin/free5gc-upfd'
    else:
        cmd = 'ps -aux | grep ./all_in_one/bin/%s' % pnf_name
    while(1):
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.read().decode().split("\n")
        if len(out)==4:
            lock = False
        else if len(out)!=4 and lock==False:
            HealPnf(pnf_name)
        '''print(len(out))
        for i in range(1,len(out)):
            print('{} : {}'.format(i,out[i]))'''
      

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