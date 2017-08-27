from flask import Flask, request, send_from_directory, make_response
from colors import *
from PIL import Image
import datetime
import time

app = Flask(__name__)

ips = {}

def get_ip():
    return request.environ['REMOTE_ADDR']

@app.route('/image.png')
def image():
    with open('image.png', 'rb') as f:
        img = f.read()
    response = make_response(img)
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/server', methods=['POST'])
def server():
    try:
        x = int(request.values.get('x'))
        y = int(request.values.get('y'))
        color = int(request.values.get('c'))
        if x not in range(128):
            return "Please do not cheeeeeeeeeat"
        if y not in range(128):
            return "Please do not cheeeeeeeeeat"
        if color not in range(16):
            return "Please do not cheeeeeeeeeat"
    except:
        return "Please do not cheeeeeeeeeat"
    ip = get_ip()
    if not ip in ips:
        ips[ip] = int(time.time()) + 25
    else:
        if ips[ip] > int(time.time()):
            return "Please do not cheeeeeeeeeat"
        else:
            ips[ip] = int(time.time()) + 25
    pic = Image.open('image.png')
    pix = pic.load()
    pix[x, y] = tuple(int(COLORS[color][i:i+2], 16) for i in (1, 3, 5))
    pic.save('image.png')
    with open('id', 'r') as f:
        q = int(f.read())
    q += 1
    pic.save('log/%06d.png' % q)
    with open('id', 'w') as f:
        f.write(str(q))
    return "Oh, wee!"
