import sys
import paramiko
import signal


def DetectPnf(pnf_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.219',22,username='jeffery', password='jeffery71')
    if pnf_name == 'upf':
        cmd = 'ps -aux | grep ./bin/free5gc-upfd'
    else:
        cmd = 'ps -aux | grep ./all_in_one/bin/%s' % pnf_name
    while(1):
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.read().decode().split("\r\n")
        print(len(out))
        for i in range(1,len(out)):
            print('{} : {}'.format(i,out[i]))
        #print(stdout.read().decode())

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