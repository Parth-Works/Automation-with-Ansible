import flask
import time
import socket

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

app = flask.Flask(__name__)

@app.route('/')
def index():
    Time= time.strftime("%H:%M:%S")
    client_port = str(flask.request.environ.get('REMOTE_PORT'))
    hostname = h_name
    host_IP = IP_address
    return Time+" This Service is from the Host: "+hostname+" ("+host_IP+") :" +client_port+".\n"
