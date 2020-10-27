import paramiko, base64,getpass,time
def reset(ip):
    key=paramiko.RSAKey.from_private_key_file('./free5gc.key')
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, 22,username='ubuntu',password='',pkey=key,compress=True)
    if ip=='172.24.4.111':
        print('reset upf')
        cmds = ['sudo kill $(pidof ./bin/free5gc-upfd)\n','cd /home/ubuntu/stage3/src/upf/lib/libgtp5gnl/tools\n','sudo ./gtp5g-link del upfgtp0\n','sudo rm /dev/mqueue/*\n','cd /home/ubuntu/stage3/src/upf/build\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/free5gc-upfd);cd /home/ubuntu/stage3/src/upf/lib/libgtp5gnl/tools;sudo ./gtp5g-link del upfgtp0;sudo rm /dev/mqueue/*;cd /home/ubuntu/stage3/src/upf/build;sudo ./bin/free5gc-upfd')
        for cmd in cmds:
            time.sleep(1)
            ssh.send(cmd)
        time.sleep(1)
    elif ip=='172.24.4.102':
        print('reset amf')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/amf);cd /home/ubuntu/stage3;sudo ./bin/amf')
    elif ip=='172.24.4.103':
        print('reset smf')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/smf);cd /home/ubuntu/stage3;sudo ./bin/smf')
    elif ip=='172.24.4.104':
        print('reset udr')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/udr);cd /home/ubuntu/stage3;sudo ./bin/udr')
    elif ip=='172.24.4.105':
        print('reset pcf')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/pcf);cd /home/ubuntu/stage3;sudo ./bin/pcf')
    elif ip=='172.24.4.106':
        print('reset udm')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/udm);cd /home/ubuntu/stage3;sudo ./bin/udm')
    elif ip=='172.24.4.107':
        print('reset nssf')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/nssf);cd /home/ubuntu/stage3;sudo ./bin/nssf')
    elif ip=='172.24.4.108':
        print('reset ausf')
        stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/ausf);cd /home/ubuntu/stage3;sudo ./bin/ausf')
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
    return 