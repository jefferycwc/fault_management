import os
import paramiko
import re
import time
class MySFTPClient(paramiko.SFTPClient):
    def put_dir(self, source, target):
        ''' Uploads the contents of the source directory to the target path. The
            target directory needs to exists. All subdirectories in source are 
            created under target.
        '''
        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                self.put(os.path.join(source, item), '%s/%s' % (target, item))
            else:
                self.mkdir('%s/%s' % (target, item), ignore_existing=True)
                self.put_dir(os.path.join(source, item), '%s/%s' % (target, item))

    def mkdir(self, path, mode=511, ignore_existing=False):
        ''' Augments mkdir by adding an option to not fail if the folder exists  '''
        try:
            super(MySFTPClient, self).mkdir(path, mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise

class RemoteConnect():
    def __init__(self,target_addr):
        self.jumpbox_addr = '192.168.1.77'
        self.jumpbox_username = 'jeffery'
        self.jumpbox_password = 'jeffery71'
        self.target_addr = target_addr

    def build_transport(self):
        key=paramiko.RSAKey.from_private_key_file('./free5gc.key')

        jumpbox=paramiko.SSHClient()
        jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumpbox.connect(self.jumpbox_addr, username=self.jumpbox_username, password=self.jumpbox_password)

        jumpbox_transport = jumpbox.get_transport()
        src_addr = (self.jumpbox_addr, 22)
        dest_addr = (self.target_addr, 22)

        while True:
            try:
                jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)
                target=paramiko.SSHClient()
                target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                target.connect(self.target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
                break
            except:
                print('connection failed')
            continue
        return target, jumpbox 
    
    def ssh_direct(self,cmds,target_username,target_password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.target_addr,22,username=target_username, password=target_password)
        chan = ssh.invoke_shell()
        for cmd in cmds:
            time.sleep(2)
            chan.send(cmd)
            while not re.search(".*\[sudo\].*",chan.recv(1024)): time.sleep(1)
                chan.send( "%s\n" % target_password )
            '''out=chan.recv(1024)
            print(out)'''
        
        time.sleep(1)
        ssh.close()

    def ssh_jump(self,cmds):
        transport, jumpbox = self.build_transport()
        chan = transport.invoke_shell()
        for cmd in cmds:
            if cmd=='sudo make install\n':
                time.sleep(20)
            else:
                time.sleep(1)
            chan.send(cmd)
            out=chan.recv(1024)
            print(out)

        time.sleep(1)
        transport.close()
        jumpbox.close()
    
    def transport_dir(self):
        transport, jumpbox = self.build_transport()
        #print('start transfering files')
        sftp = MySFTPClient.from_transport(transport.get_transport())
        sftp.mkdir('/home/ubuntu/stage3/src/upf/build', ignore_existing=True)
        sftp.put_dir('/home/free5gmano/fault_management/build', '/home/ubuntu/stage3/src/upf/build')
        sftp.close()
        transport.close()
        jumpbox.close()
        #print('finish transfering files')

