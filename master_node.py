from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/healvnf', methods=['GET'])
def healvnf():
    id = request.args.get('id')
    return "<h1>heal vnf successfully!</h1>"
app.run(host='192.168.1.219',port=5010)