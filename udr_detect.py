import requests,time,paramiko, base64,getpass,time
import json
from params import OPENSTACK_IP,OS_AUTH_URL,OS_USER_DOMAIN_NAME,OS_USERNAME,OS_PASSWORD,OS_PROJECT_DOMAIN_NAME,OS_PROJECT_NAME
from tacker_params import TACKER_IP,TACKER_OS_AUTH_URL,TACKER_OS_USER_DOMAIN_NAME,TACKER_OS_USERNAME,TACKER_OS_PASSWORD,TACKER_OS_PROJECT_DOMAIN_NAME,TACKER_OS_PROJECT_NAME

#response = requests.get("http://192.168.1.134/identity/v3/auth/tokens")

class TackerAPI():
    def __init__(self):
        self.TACKER_IP = TACKER_IP
        self.TACKER_OS_AUTH_URL = TACKER_OS_AUTH_URL
        self.TACKER_OS_USER_DOMAIN_NAME = TACKER_OS_USER_DOMAIN_NAME
        self.TACKER_OS_USERNAME = TACKER_OS_USERNAME
        self.TACKER_OS_PASSWORD = TACKER_OS_PASSWORD
        self.TACKER_OS_PROJECT_DOMAIN_NAME = TACKER_OS_PROJECT_DOMAIN_NAME
        self.TACKER_OS_PROJECT_NAME = TACKER_OS_PROJECT_NAME
        self.ary_data = []
        self.nsd_id = ''
        self.nsd_name = ''
        self.get_token_result = ''
        self.project_id = ''

    def get_token(self):
        # print("\nGet token:")
        self.get_token_result = ''
        get_token_url = self.TACKER_OS_AUTH_URL + 'auth/tokens'
        get_token_body = {
            'auth': {
                'identity': {
                    'methods': [
                        'password'
                    ],
                    'password': {
                        'user': {
                            'domain': {
                                'name': self.TACKER_OS_USER_DOMAIN_NAME
                            },
                            'name': self.TACKER_OS_USERNAME,
                            'password': self.TACKER_OS_PASSWORD
                        }
                    }
                },
                'scope': {
                    'project': {
                        'domain': {
                            'name': self.TACKER_OS_PROJECT_DOMAIN_NAME
                        },
                        'name': self.TACKER_OS_PROJECT_NAME
                    }
                }
            }
        }
        get_token_response = requests.post(get_token_url, data=json.dumps(get_token_body))
        #print("Get Tacker token status: " + str(get_token_response.status_code))
        self.get_token_result = get_token_response.headers['X-Subject-Token']
        return self.get_token_result

    def get_project_id(self, project_name):
        # print("\nGet Project ID:")
        self.project_id = ''
        get_project_list_url = self.TACKER_OS_AUTH_URL + 'projects'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_project_list_response = requests.get(get_project_list_url, headers=headers)
        print("Get Tacker project list status: " + str(get_project_list_response.status_code))
        get_project_list_result = get_project_list_response.json()['projects']
        #print(get_project_list_result)
        for project in get_project_list_result:
            if project['name'] == project_name:
                self.project_id = project['id']
            pass
        print("Project ID:" + self.project_id)
        return self.project_id

    

    def create_vnf(self, vnf_name, vnfd_name, vim_name):
        post_create_vnf_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        tenant_id = self.get_project_id(self.TACKER_OS_PROJECT_NAME)
        vnfd_id = self.get_vnfd_id(vnfd_name)
        vnf_description = 'udr'
        vim_id = self.get_vim_id(vim_name)
        vnf_body = {
                'vnf': {
                    'name': vnf_name,
                    'description': vnf_description,
                    'tenant_id': tenant_id,
                    'vnfd_id': vnfd_id,
                    'vim_id': vim_id,
                }
        }
	
        #print(nsd_body)
        res_create_vnf = requests.post(post_create_vnf_url, data=json.dumps(vnf_body), headers=headers)
        print('Create VNF status: ' + str(res_create_vnf.status_code))
        vnf_id = res_create_vnf.json()['vnf']['id']
        create_vnf_status = res_create_vnf.json()['vnf']['status']
        count =0
        while create_vnf_status !='ACTIVE' and create_vnf_status != 'ERROR':
            show_vnf_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs/' + vnf_id
            res_show_vnf = requests.get(show_vnf_url, headers=headers).json()
            create_vnf_status = res_show_vnf['vnf']['status']
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('create udr successfully!!')
        #result = response.json()
        #print(result)

    

    def list_vim(self):
        get_vim_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vims'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vim_list_response = requests.get(get_vim_list_url, headers=headers)
        print("Get Tacker vim list status: " + str(get_vim_list_response.status_code))
        get_vim_list_result = get_vim_list_response.json()
        #text = get_vim_list_response.text
        #print(get_vim_list_result)
        #print(text)
        return get_vim_list_result     

    def get_vim_id(self, vim_name):
        vim_list = self.list_vim()
        #print(vim_list)
        vim_id = None
        for vim in vim_list['vims']:
            if vim['name'] == vim_name:
                vim_id = vim['id']
                print vim_id
            pass
        return vim_id

    

    def list_vnfd(self):
        get_vnfd_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfds'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vnfd_list_response = requests.get(get_vnfd_list_url, headers=headers)
        print("Get Tacker vnfd list status: " + str(get_vnfd_list_response.status_code))
        get_vnfd_list_result = get_vnfd_list_response.json()
        #text = get_nsd_list_response.text
        #print(get_nsd_list_result)
        #print(text)
        return get_vnfd_list_result    

    def get_vnfd_id(self, vnfd_name):
        vnfd_list = self.list_vnfd()
        #print(vnfd_list)
        vnfd_id = None
        for vnfd in vnfd_list['vnfds']:
            if vnfd['name'] == vnfd_name:
                vnfd_id = vnfd['id']
                print vnfd_id
            pass
        return vnfd_id

    def generate_node_templates(self, number_of_vnf):
        node_templates = {}
        for i in range(number_of_vnf):
            vnf_s = "VNF" + str(i+1)
            vnf_t = "tosca.nodes.nfv.VNF" + str(i+1)
            vnf_d = {
                vnf_s: {
                    "type":vnf_t,
                }
            }
        node_templates.update(vnf_d)
        #print(vnf_d)
	
        print(node_templates)
        return node_templates

    def list_vnf(self):
        get_vnf_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vnf_list_response = requests.get(get_vnf_list_url, headers=headers)
        print("Get Tacker vnf list status: " + str(get_vnf_list_response.status_code))
        vnf_status = {}
        get_vnf_list_result = get_vnf_list_response.json()
        get_vnf_list_result = get_vnf_list_result['vnfs']
        #print('len: {}'.format(len(get_vnf_list_result)))
        for i in range(len(get_vnf_list_result)):
            #print('i: {}'.format(i))
            #print(get_vnf_list_result[i]['name'])
            vnf_status[get_vnf_list_result[i]['name']] = get_vnf_list_result[i]['status']
            #vnf_name[i] = get_vnf_list_result[i]['name']
        print('nrf status: {}'.format(vnf_status['nrf']))
        #for i in rnage(len(vnf_name)):
        #    print(vnf_name[i])
        #text = get_vnf_list_response.text
        #print(get_vnf_list_result)
        #print(text)
        return get_vnf_list_result
    def get_vnf_id(self,get_vnf_list_result,name):
        id = 0
        get_vnf_list_result = get_vnf_list_result['vnfs']
        for i in range(len(get_vnf_list_result)):
            if get_vnf_list_result[i]['description'] == 'udr':
                return get_vnf_list_result[i]['id']
        return 0
        #return id
    def get_udr_status(self,udr_id):
        get_vnf_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs/' + str(udr_id)
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vnf_response = requests.get(get_vnf_url, headers=headers)
        print("Get udr status: " + str(get_vnf_response.status_code))
        return str(get_vnf_response.status_code)
        #get_vnf_result = get_vnf_response.json()['vnf']
        #return get_vnf_result['status']
        
    def udr_detect(self):
        get_vnf_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vnf_list_response = requests.get(get_vnf_list_url, headers=headers)
        get_vnf_list_result = get_vnf_list_response.json()
        name = 'udr'
        vnf_id = self.get_vnf_id(get_vnf_list_result,name)
        if vnf_id==0:
            self.create_vnf('udr','udr','jefferyvim')
        #print('id: {}'.format(vnf_id))
        vnf_status = self.get_udr_status(vnf_id) 
        if vnf_status!='200':
            self.create_vnf('udr','udr','jefferyvim')
        return 
        #print('udr status: {}'.format(vnf_status))
    def list_ns(self):
        get_ns_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/nss'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_ns_list_response = requests.get(get_ns_list_url, headers=headers)
        print("Get Tacker ns list status: " + str(get_ns_list_response.status_code))
        get_ns_list_result = get_ns_list_response.json()
        #text = get_vnf_list_response.text
        print(get_ns_list_result)
        #print(text)
        return get_ns_list_result
        
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
               
    def get_udr_status(self,instance_id):
        get_udr_status_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_instance_status_response = requests.get(get_udr_status_url, headers=headers)
        #print("Get udr instance status: " + str(get_instance_status_response.status_code))
        #print("get instance result: {}".format(get_instance_status_response.json()))
        status = get_instance_status_response.json()['server']['status']
        return status

    def unpause_instance(self,instance_id):
        unpause_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id + '/action'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        null = None
        req_body = {
            'unpause' : null
        }
        res = requests.post(unpause_instance_url, data=json.dumps(req_body), headers=headers)
        #print("resume udr instance status: "+ str(res.status_code))
        #print(res)
        count=0
        while 1:
            if self.get_udr_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('unpause udr successfully!!')
        #restart()

    def resume_instance(self,instance_id):
        resume_instance_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id + '/action'
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        null = None
        req_body = {
            'resume' : null
        }
        res = requests.post(resume_instance_url, data=json.dumps(req_body), headers=headers)
        #print("resume udr instance status: "+ str(res.status_code))
        #print(res)
        count=0
        while 1:
            if self.get_udr_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('resume udr successfully!!')
        restart(instance_id)
    
    def reboot_instance(self,instance_id):
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
            if self.get_udr_status(instance_id)=='ACTIVE':
                break
            time.sleep(1)
            count = count+1
            print('wait ' + str(count) + 's')
        print('reboot udr successfully!!')
        restart(instance_id)

    def udr_detect(self):
        instance_id = self.get_instance_id('free5gc-udr-VNF')
        #print('udr instance id: {}'.format(instance_id))
        udr_status = self.get_udr_status(instance_id)
        if udr_status!='ACTIVE':
            print("udr instance status: {}".format(udr_status))
        if udr_status=='PAUSED':
            self.unpause_instance(instance_id)
        elif udr_status=='SHUTOFF':
            self.reboot_instance(instance_id)
        elif udr_status=='SUSPENDED':
            self.resume_instance(instance_id)
def restart(instance_id):
    key=paramiko.RSAKey.from_private_key_file('./free5gc.key')
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("ready to ssh")
    #time.sleep(3)
    #test=OpenStackAPI()
    #status=test.get_udr_status(instance_id)
    #while 1:
    #    print("the status is: {}".format(status))
    #    if status =='ACTIVE':
    #        break
    #    status=test.get_udr_status()
    #time.sleep(10)
    count=0
    while 1:
        time.sleep(1)
        count = count+1
        print('wait ' + str(count) + 's')
        if count==20:
            break
    client.connect('172.24.4.103', 22,username='ubuntu',password='',pkey=key,compress=True)
    stdin,stdout,stderr = client.exec_command('cd /home/ubuntu/stage3;sudo ./bin/udr')
    #if stderr:
    #    print stderr.read()
    #else:
    #    print stdout.read()
    #print stdout.read()
    count=0
    while 1:
        time.sleep(1)
        count = count+1
        print('wait ' + str(count) + 's')
        if count==10:
            break
    client.close 
    print("ssh connection close")
    return 

if __name__ == '__main__':
    print('start')
    #test = TackerAPI()
    #test.udr_detect()
    #while 1:
    #    test.udr_detect()
    test = OpenStackAPI()
    while 1:
        test.udr_detect()
    #test = OpenStackAPI()
    #instance_id = test.get_instance_id('free5gc-udr-VNF')
    #restart(instance_id)



