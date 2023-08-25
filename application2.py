import flask
import time
import socket
import subprocess

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

app = flask.Flask(__name__)

@app.route('/')
def index():
    Time = time.strftime("%H:%M:%S")
    client_port = str(flask.request.environ.get('REMOTE_PORT'))
    hostname = h_name
    host_IP = IP_address

    # Retrieve server uptime using the uptime command
    uptime_output = subprocess.check_output(['uptime']).decode('utf-8')
    uptime_info = uptime_output.split(',')[0].strip()

    return (Time + " This Service is from the Host: " + hostname +
            " (" + host_IP + "):" + client_port + ".\n" +
            "Server Uptime: " + uptime_info + ".\n")

if _name_ == '__main__':
    app.run(host='0.0.0.0', port=8080)
