from flask import Flask,render_template,request,jsonify
import requests
from params import OPENSTACK_IP,OS_AUTH_URL,OS_USER_DOMAIN_NAME,OS_USERNAME,OS_PASSWORD,OS_PROJECT_DOMAIN_NAME,OS_PROJECT_NAME

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/healvnf', methods=['POST'])
def HandleHealvnf():
    data = request.get_json()
    id = data['id']
    status = data['status']
    print('id = {id} status = {status}'.format(id=id,status=status))
    if status == 'paused':
        unpause(id)
    elif status == 'suspend':
        resume(id)
    elif status == 'shutoff':
        reboot(id)
    result = 'yes'
    return result
app.run(host='192.168.1.219',port=5010)

def unpause():
    pass

def resume():
    pass

def reboot():
    pass