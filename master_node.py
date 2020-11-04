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
    data = request.get_json()
    id = data['id']
    status = data['status']
    print('id = {id} status = {status}'.format(id=id,status=status))
    new_item = OpenStackAPI()
    if status == 'paused':
        result = new_item.unpause(id)
    elif status == 'suspended':
        result = new_item.resume(id)
    elif status == 'shutoff':
        result = new_item.reboot(id)
    if result:
        return 'successful'
    else:
        return 'failed'
app.run(host='192.168.1.219',port=5010)

