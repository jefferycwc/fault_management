import psutil
import sys
import socket
import requests
import json
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            #print(pinfo)
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower() :
                listOfProcessObjects.append(pinfo)
        except:
            print("Unexpected error:", sys.exc_info()[0])
    return listOfProcessObjects

if __name__ == "__main__":
    #process_name = sys.argv[1]
    hostname = socket.gethostname()
    url = 'http://192.168.1.103:5010/alarm'
    body = {
        'vnf_name': hostname
    }
    lock = 0
    print(hostname)
    while 1:
        listOfProcessIds = findProcessIdByName(hostname)
        if len(listOfProcessIds) > 0:
            '''print('Process Exists | PID and other details are')
            for elem in listOfProcessIds:
                processID = elem['pid']
                processName = elem['name']
                print(processID ,processName)'''
            lock=0
        else :
            if lock==0:
                print('No Running Process found with given text')
                response = requests.post(url,json=body)
                lock=1
