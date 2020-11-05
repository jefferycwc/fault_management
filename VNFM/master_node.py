from flask import Flask,render_template,request,jsonify
import requests
from HandleHealVnf import OpenStackAPI
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/healvnf', methods=['POST'])
def ReceiveHealVnfRequest():
    print('Receive HealVnfResponse')
    data = request.get_json()
    id = data['id']
    cause = data['cause']
    name = data['name']
    print('vnf instance id = {id} cause = {cause}'.format(id=id,cause=cause))
    new_item = OpenStackAPI()
    if cause == 'paused':
        result = new_item.unpause(id)
    elif cause == 'suspended':
        result = new_item.resume(id,name)
    elif cause == 'shutoff':
        result = new_item.reboot(id,name)
    print('Send HealVnfResponse')
    if result:
        return 'successful'
    else:
        return 'failed'
app.run(host='192.168.1.219',port=5010)

