import multiprocessing
import os
def worker(arg):
    os.system(arg)
if __name__ == '__main__':
    files = ["python3 mongo_detect.py","python3 nrf_detect.py","python3 amf_detect.py","python3 smf_detect.py","python3 udr_detect.py","python3 pcf_detect.py","python3 udm_detect.py","python3 nssf_detect.py","python3 ausf_detect.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()