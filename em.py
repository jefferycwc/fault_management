import multiprocessing

if __name__ == '__main__':
    files = ["./nrf_detect.py","./amf_detect.py","./smf_detect.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()