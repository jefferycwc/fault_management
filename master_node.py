import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


app.run(host='192.168.1.219',port=5010)