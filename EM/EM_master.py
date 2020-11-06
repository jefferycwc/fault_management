import multiprocessing
from multiprocessing import Process, Pool
import os
import signal
import sys
def worker(arg):
    os.system(arg)

def kill_process():
    process_name = ['EM_mongo.py','EM_upf.py','EM_nrf.py','EM_amf.py','EM_smf.py','EM_udr.py','EM_pcf.py','EM_udm.py','EM_nssf.py','EM_ausf.py','EM_master.py']
    for process in process_name:
        print(process)
        for line in os.popen("ps ax | grep " + process + " | grep -v grep"):
            fields = line.split() 
            pid = fields[0]
            print(pid)
            os.kill(int(pid), signal.SIGKILL)     
            
if __name__ == "__main__":
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    pool =Pool(10)
    cmds = ["python EM_mongo.py","python EM_upf.py","python EM_nrf.py","python EM_amf.py","python EM_smf.py","python EM_udr.py","python EM_pcf.py","python EM_udm.py","python EM_nssf.py","python EM_ausf.py"]
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        result=pool.map_async(worker,cmds).get(2000)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
        kill_process()
    else:
        print("Normal termination")
        pool.close()
    pool.join()
