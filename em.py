#import multiprocessing
from multiprocessing import Process, Pool
import os
import signal
import sys
def worker(arg):
    try:
        os.system(arg)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating worker")

if __name__ == '__main__':
    files = ["python mongo_detect.py","python upf_detect.py","python nrf_detect.py","python amf_detect.py","python smf_detect.py","python udr_detect.py","python pcf_detect.py","python udm_detect.py","python nssf_detect.py","python ausf_detect.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
'''if __name__ == "__main__":
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    pool =Pool(10)
    cmds = ["python mongo_detect.py","python upf_detect.py","python nrf_detect.py","python amf_detect.py","python smf_detect.py","python udr_detect.py","python pcf_detect.py","python udm_detect.py","python nssf_detect.py","python ausf_detect.py"]
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        result=pool.map_async(worker,cmds).get(9999)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    else:
        print("Normal termination")
        pool.close()
    pool.join()'''
