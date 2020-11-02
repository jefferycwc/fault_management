import multiprocessing
import os
import signal
import sys
def worker(arg):
    signal.signal(signal.SIGINT, signal_handler)
    os.system(arg)
    
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    # for p in jobs:
    #     p.terminate()
    sys.exit(0)
if __name__ == '__main__':
    files = ["python mongo_detect.py","python upf_detect.py","python nrf_detect.py","python amf_detect.py","python smf_detect.py","python udr_detect.py","python pcf_detect.py","python udm_detect.py","python nssf_detect.py","python ausf_detect.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()