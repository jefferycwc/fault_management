import requests,json
def SendHealVnfRequest(id,status,name):
    body = {
        'id' : id,
        'status' : status,
        'name' : name
    }
    url = 'http://192.168.1.219:5010/healvnf'
    print('Send HealVnfRequest')
    response = requests.post(url,json=body)
    print('Receive HealVnfResponse, result is {}'.format(response.text))