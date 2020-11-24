import psutil
import sys
import socket
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        #try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            #print(pinfo)
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower() :
                listOfProcessObjects.append(pinfo)
        #except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
        #    pass
    return listOfProcessObjects

if __name__ == "__main__":
    process_name = sys.argv[1]
    hostname = socket.gethostname()
    print(hostname)
    '''while 1:
        listOfProcessIds = findProcessIdByName(process_name)
        if len(listOfProcessIds) > 0:
            print('Process Exists | PID and other details are')
            for elem in listOfProcessIds:
                processID = elem['pid']
                processName = elem['name']
                print(processID ,processName)
        else :
            print('No Running Process found with given text')'''