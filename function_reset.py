import paramiko, base64,getpass,time
def reset(ip):
    key=paramiko.RSAKey.from_private_key_file('./free5gc.key')
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, 22,username='ubuntu',password='',pkey=key,compress=True)
    if ip=='192.168.2.111':
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/free5gc-upfd);cd /home/ubuntu/stage3/src/upf/build;sudo ./bin/free5gc-upfd')
    #stdin,stdout,stderr = client.exec_command('cd /home/ubuntu/stage3;ls')
    #print stdout.read()
    #ssh=client.invoke_shell()
    #cmds=['cd /home/ubuntu/stage3/src/upf/build\n','sudo ./free5gc-upfd','ls']
    #for cmd in cmds:
    #        time.sleep(1)
    #        ssh.send(cmd)
    #        out = ssh.recv(1024)
    #        print ('output: {}'.format(out))
    #        time.sleep(5)
    #ssh.send('cd /home/ubuntu/stage3/src/upf\n')
    #ssh.send('ls\n')
    #out = ssh.recv(1024)
    #print out
    #stdin,stdout,stderr = client.exec_command('mkdir build')
    #print stdout.read()
    #if stderr:
    #    print stderr.read()
    time.sleep(1)
    client.close 