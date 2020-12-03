import requests,time,paramiko, base64,getpass
import json
import os
import sys
import threading
from params.openstack_params import OPENSTACK_IP,OS_AUTH_URL,OS_USER_DOMAIN_NAME,OS_USERNAME,OS_PASSWORD,OS_PROJECT_DOMAIN_NAME,OS_PROJECT_NAME
from params.tacker_params import *
from PublishHandler import publisher

import ctypes

SYS_gettid = 186
libc = ctypes.cdll.LoadLibrary('libc.so.6')

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
        #print("Get Tacker project list status: " + str(get_project_list_response.status_code))
        get_project_list_result = get_project_list_response.json()['projects']
        #print(get_project_list_result)
        for project in get_project_list_result:
            if project['name'] == project_name:
                self.project_id = project['id']
            pass
        #print("Project ID:" + self.project_id)
        return self.project_id

    def get_vnf_status(self,vnf_id):
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        tenant_id = self.get_project_id(self.TACKER_OS_PROJECT_NAME)
        get_vnf_status_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs/' + vnf_id
        response = requests.get(get_vnf_status_url,headers=headers)
        status = response.json()['vnf']['status']
        return status
    
    def list_vnf(self):
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_vnf_list_url = 'http://' + self.TACKER_IP + ':9890/v1.0/vnfs'
        get_vnf_list_response = requests.get(get_vnf_list_url,headers=headers)
        get_vnf_list_result = get_vnf_list_response.json()
        return get_vnf_list_result

    def get_vnf_id(self,vnf_name):
        vnf_list = self.list_vnf()
        vnf_id = None
        vnf_description = 'VNFD:'+ vnf_name
        for vnf in vnf_list['vnfs']:
            if vnf['description']==vnf_description:
                vnf_id=vnf['id']
            pass
        return vnf_id

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
        self.lock = 0

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
        #print("Project ID:" + self.project_id)
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
        #print('thread exit, id:{}'.format(threading.get_ident()))
        #os._exit(0)

    def get_instance_status(self,instance_id):
        try:
            get_instance_status_url = 'http://' + self.OPENSTACK_IP + '/compute/v2.1/servers/' + instance_id
        except Exception, e:
            #print >> sys.stderr, "Exception: %s" % str(e)
            sys.exit(1)
        token = self.get_token()
        headers = {'X-Auth-Token': token}
        get_instance_status_response = requests.get(get_instance_status_url, headers=headers)
        try:
            status = get_instance_status_response.json()['server']['status']
        except Exception, e:
            #print >> sys.stderr, "Exception: %s" % str(e)
            sys.exit(1)
        return status

    def instance_detect(self,vnf_name,vnf_id):
        instance_id = self.get_instance_id(vnf_name)
        instance_status = self.get_instance_status(instance_id)
        if instance_status=='ACTIVE':
            self.lock=0

        if instance_status=='PAUSED' and self.lock==0:
            publisher(vnf_id,instance_id,'paused',vnf_name,'report')
            self.lock=1
        elif instance_status=='SHUTOFF' and self.lock==0:
            publisher(vnf_id,instance_id,'shutoff',vnf_name,'report')
            self.lock=1
        elif instance_status=='SUSPENDED' and self.lock==0:
            publisher(vnf_id,instance_id,'suspended',vnf_name,'report')
            self.lock=1

def start(vnf_name,vnf_id):
    tid = libc.syscall(SYS_gettid)
    #print('thread id: {}'.format(tid))
    tacker = TackerAPI()
    vnf_status = tacker.get_vnf_status(vnf_id)
    while(vnf_status!='ACTIVE'):
        #print('vnf status: {}'.format(vnf_status))
        time.sleep(1)
        vnf_status = tacker.get_vnf_status(vnf_id)
    #print('start detecting {}'.format(vnf_name))
    openstack = OpenStackAPI()
    while 1:
        openstack.instance_detect(vnf_name,vnf_id)
