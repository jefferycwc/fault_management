import requests,json
from ssh_jump import ssh_jump
from params import OPENSTACK_IP,OS_AUTH_URL,OS_USER_DOMAIN_NAME,OS_USERNAME,OS_PASSWORD,OS_PROJECT_DOMAIN_NAME,OS_PROJECT_NAME
class OpenStackAPI():
    def __init__(self):
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

    def unpause(self,id):
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

    def resume(self,id):
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
        return restart(instance_id)

    def reboot(self,id):
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
        return restart(instance_id)

def restart(instance_id):
    print('resart instance')
    count=0
    while 1:
        time.sleep(1)
        count = count+1
        print('wait ' + str(count) + 's')
        if count==25:
            break
    cmds=['cd /home/ubuntu/stage3\n','sudo nohup ./bin/instance & \n','exit\n']
    ssh_jump('172.24.4.105',cmds)
    print('resart instance successfully')
    return True