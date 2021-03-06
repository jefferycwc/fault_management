import requests,json,time
import sys
from remote_connect import RemoteConnect
from function_reset import reset
class OpenStackAPI():
    def __init__(self):
        self.OPENSTACK_IP = '192.168.1.77'
        self.OS_AUTH_URL = 'http://192.168.1.77/identity'
        self.OS_USER_DOMAIN_NAME = 'Default'
        self.OS_USERNAME = 'admin'
        self.OS_PASSWORD = 'secret'
        self.OS_PROJECT_DOMAIN_NAME = 'Default'
        self.OS_PROJECT_NAME = 'admin'
        self.ary_data = []
        self.nsd_id = ''
        self.nsd_name = ''
        self.get_token_result = ''
        self.project_id = ''

    def get_token(self):
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
        for ins in instance_list:
            if ins['name'] == ins_name:
                return ins['id']

    def get_instance_status(self,instance_id):
        get_pcf_status_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_instance_status_response = requests.get(get_pcf_status_url, headers=headers)
        status = get_instance_status_response.json()['server']['status']
        return status

    def unpause(self,instance_id):
        unpause_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id + '/action'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        null = None
        req_body = {
            'unpause' : null
        }
        res = requests.post(unpause_instance_url, data=json.dumps(req_body), headers=headers)
        count=0
        while 1:
            if self.get_instance_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('unpause instance successfully!!')
        return True

    def resume(self,instance_id,cause,name,cmds,ip):
        resume_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id + '/action'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        null = None
        req_body = {
            'resume' : null
        }
        res = requests.post(resume_instance_url, data=json.dumps(req_body), headers=headers)
        count=0
        while 1:
            if self.get_instance_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('resume instance successfully!!')
        return self.restart(name,cmds,ip,cause)

    def reboot(self,instance_id,cause,name,cmds,ip):
        reboot_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id + '/action'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        null = None
        req_body = {
            'reboot' : {
                'type' : 'HARD'
            }
        }
        res = requests.post(reboot_instance_url, data=json.dumps(req_body), headers=headers)
        count=0
        while 1:
            if self.get_instance_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('reboot instance successfully!!')
        return self.restart(name,cmds,ip,cause)

    def restart(self,name,cmds,ip,cause):
        print('resart instance')

        if name == 'smf':
            self.Reset_for_SMF()
        connector = RemoteConnect(ip)
        connector.ssh_jump(cmds)
        if cause != 'vnf stop running' or cause!='pause':
            cmds = ['sudo service VnfDetect restart\n','exit\n']
            connector.ssh_jump(cmds)
        #print('resart instance successfully')
        if name == 'upf':
            self.Reset_for_UPF()
        elif name == 'nrf':
            self.Reset_for_NRF()
        return True

    def Reset_for_UPF(self):
        ip ='172.24.4.103'
        reset(ip)

    def Reset_for_SMF(self):
        ip = '172.24.4.111'
        reset(ip)

    def Reset_for_NRF(self):
        IP = ['172.24.4.111','172.24.4.102','172.24.4.103','172.24.4.104','172.24.4.105','172.24.4.106','172.24.4.107','172.2.4.4.108']
        for ip in IP:
            reset(ip)