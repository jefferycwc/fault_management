import multiprocessing
import os
def worker(arg):
    os.system(arg)
if __name__ == '__main__':
    files = ["python nrf_detect.py","python amf_detect.py","python smf_detect.py","python udr_detect.py","python pcf_detect.py","python udm_detect.py","python nssf_detect.py","python ausf_detect.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()