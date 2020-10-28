import os
import paramiko

key=paramiko.RSAKey.from_private_key_file('./free5gc.key')

jumpbox_addr = '192.168.1.77'
#jumpbox_private_addr = '10.0.5.10'
target_addr = '172.24.4.104'

jumpbox=paramiko.SSHClient()
jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jumpbox.connect(jumpbox_addr, username='openstack', password='0000')

jumpbox_transport = jumpbox.get_transport()
src_addr = (jumpbox_addr, 22)
dest_addr = (target_addr, 22)
jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)

target=paramiko.SSHClient()
target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target.connect(target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
ssh = target.invoke_shell()
cmds = ['ls\n']
for cmd in cmds:
    time.sleep(1)
    ssh.send(cmd)
    out=ssh.recv(1024)
    print out
time.sleep(1)

target.close()
jumpbox.close()

