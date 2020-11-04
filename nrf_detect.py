import requests,time,paramiko, base64,getpass,time
import json
from params import OPENSTACK_IP,OS_AUTH_URL,OS_USER_DOMAIN_NAME,OS_USERNAME,OS_PASSWORD,OS_PROJECT_DOMAIN_NAME,OS_PROJECT_NAME
from tacker_params import TACKER_IP,TACKER_OS_AUTH_URL,TACKER_OS_USER_DOMAIN_NAME,TACKER_OS_USERNAME,TACKER_OS_PASSWORD,TACKER_OS_PROJECT_DOMAIN_NAME,TACKER_OS_PROJECT_NAME
from ssh_jump import ssh_jump 
from function_reset import reset
import os

class OpenStackAPI():
    def __init__(self):
        #super().__init__()
        self.OPENSTACK_IP = OPENSTACK_IP
        self.OS_AUTH_URL = OS_AUTH_URL
        self.OS_USER_DOMAIN_NAME = OS_USER_DOMAIN_NAME
        self.OS_USERNAME = OS_USERNAME
        self.OS_PASSWORD = OS_PASSWORD
        self.OS_PROJECT_DOMAIN_NAME = OS_PROJECT_DOMAIN_NAME
        self.OS_PROJECT_NAME = OS_PROJECT_NAME
        self.ary_data = []
        self.nsd_id = ''
        self.nsd_name = ''
        self.get_token_result = ''
        self.project_id = ''

    def get_token(self):
        # print("\nGet token:")
        self.get_token_result = ''
        get_token_url = self.OS_AUTH_URL + '/v3/auth/tokens'
        get_token_body = {
            'auth': {
                'identity': {
                    'methods': [
                        'password'
                    ],
                    'password': {
                        'user': {
                            'domain': {
                                'name': self.OS_USER_DOMAIN_NAME
                            },
                            'name': self.OS_USERNAME,
                            'password': self.OS_PASSWORD
                        }
                    }
                },
                'scope': {
                    'project': {
                        'domain': {
                            'name': self.OS_PROJECT_DOMAIN_NAME
                        },
                        'name': self.OS_PROJECT_NAME
                    }
                }
            }
        }
        get_token_response = requests.post(get_token_url, data=json.dumps(get_token_body))
        #print("Get OpenStack token status: " + str(get_token_response.status_code))
        self.get_token_result = get_token_response.headers['X-Subject-Token']
        return self.get_token_result

    def get_project_id(self, project_name):
        # print("\nGet Project ID:")
        self.project_id = ''
        get_project_list_url = self.OS_AUTH_URL + '/v3/projects'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_project_list_response = requests.get(get_project_list_url, headers=headers)
        print("Get OpenStack project list status: " + str(get_project_list_response.status_code))
        get_project_list_result = get_project_list_response.json()['projects']
        #print(get_project_list_result)
        for project in get_project_list_result:
            if project['name'] == project_name:
                self.project_id = project['id']
            pass
        print("Project ID:" + self.project_id)
        return self.project_id
    
    def list_instance(self):
        list_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_instance_list_response = requests.get(list_instance_url, headers=headers)
        #print("Get OpenStack instance list status: " + str(get_instance_list_response.status_code))
        get_instance_list_result = get_instance_list_response.json()
        #print('check1')
        #print(get_instance_list_result)
        return get_instance_list_result
    
    def get_instance_id(self,ins_name):
        instance_list = self.list_instance()['servers']
        #print('check2')
        #print(instance_list)
        #print('check3')
        for ins in instance_list:
            #print('ins name: {}'.format(ins[i]['name']))
            if ins['name'] == ins_name:
                #print('match!!')
                return ins['id']
               
    def get_nrf_status(self,instance_id):
        get_nrf_status_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_instance_status_response = requests.get(get_nrf_status_url, headers=headers)
        #print("Get nrf instance status: " + str(get_instance_status_response.status_code))
        #print("get instance result: {}".format(get_instance_status_response.json()))
        status = get_instance_status_response.json()['server']['status']
        return status

    def nrf_detect(self):
        instance_id = self.get_instance_id('free5gc-nrf-VNF')
        #print('nrf instance id: {}'.format(instance_id))
        nrf_status = self.get_nrf_status(instance_id)
        if nrf_status!='ACTIVE':
            print("nrf instance status: {}".format(nrf_status))
        if nrf_status=='PAUSED':
            HealVnfRequest(instance_id,'paused','nrf')
            #self.unpause_instance(instance_id)
        elif nrf_status=='SHUTOFF':
            HealVnfRequest(instance_id,'shutoff','nrf')
            #self.reboot_instance(instance_id)
        elif nrf_status=='SUSPENDED':
            HealVnfRequest(instance_id,'suspended','nrf')
            #self.resume_instance(instance_id)
            
def HealVnfRequest(id,status,name):
    body = {
        'id' : id,
        'status' : status,
        'name' : name
    }
    url = 'http://192.168.1.219:5010/healvnf'
    response = requests.post(url,json=body)
    print(response.text)
    IP = ['172.24.4.110','172.24.4.102','172.24.4.103','172.24.4.104','172.24.4.105','172.24.4.106','172.24.4.107','172.2.4.4.108']
    for ip in IP:
        reset(ip)

if __name__ == '__main__':
    print('EM_nrf start')
    #test = TackerAPI()
    #test.nrf_detect()
    #while 1:
    #    test.nrf_detect()
    test = OpenStackAPI()
    while 1:
        test.nrf_detect()
    #test = OpenStackAPI()
    #instance_id = test.get_instance_id('free5gc-nrf-VNF')
    #restart(instance_id)



