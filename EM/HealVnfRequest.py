import requests,json
def SendHealVnfRequest(id,cause,name):
    body = {
        'id' : id,
        'cause' : cause,
        'name' : name
    }
    url = 'http://192.168.1.219:5010/healvnf'
    print('Send HealVnfRequest to Master Node')
    response = requests.post(url,json=body)
    print('Receive HealVnfResponse from Master Node from VNFM'.format(name))
    return
