import sys
import paramiko
import signal
def DetectPnf(pnf_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.219',22,username='jeffery', password='jeffery71')
    while(1):
        stdin, stdout, stderr = ssh.exec_command('ps -aux | grep %s' % pnf_name)
        out = stdout.read().decode()
        print(len(out))
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