import paramiko
import os

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

def transport_dir(target_addr):
        key=paramiko.RSAKey.from_private_key_file('./free5gc.key')
        jumpbox=paramiko.SSHClient()
        jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumpbox.connect('192.168.1.77', username='jeffery', password='jeffery71')

        jumpbox_transport = jumpbox.get_transport()
        src_addr = ('192.168.1.77', 22)
        dest_addr = (target_addr, 22)

        #count = 0
        while True:
            try:
                jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)
                target=paramiko.SSHClient()
                target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                target.connect(target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
                #time.sleep(1)
                #count = count + 1
                #print(count)
                break
            except:
                print('connection failed')
            continue
        print('start transfering files')
        sftp = MySFTPClient.from_transport(target)
        sftp.mkdir('/home/ubuntu/stage3/src/upf/build', ignore_existing=True)
        sftp.put_dir('/home/free5gmano/fault_management/build', '/home/ubuntu/stage3/src/upf/build')
        sftp.close()
        print('finish transfering files')