import requests,json
def SendHealVnfRequest(id,cause,name):
    body = {
        'id' : id,
        'cause' : cause,
        'name' : name
    }
    url = 'http://192.168.1.103:5010/healvnf'
    print('Send HealVnfRequest to VNFM')
    response = requests.post(url,json=body)
    print('Receive HealVnfResponse from VNFM'.format(name))
    return
