from flask import Flask, request
from flask_cors import CORS
import json
from PIL import Image
import base64
import io
import os
import shutil
import time
import sys
from Facerec import facerec
from AddFaces import addface

app = Flask(__name__)
CORS(app)


@app.route('/addnew', methods=['POST', 'GET'])
def addnew():
    if request.method == 'POST':
        req = request.get_json()
        if os.path.exists('./img.jpeg'):
            resp = addface(req['data'], './img.jpeg')
        else:
            resp = "Click image before submitting."
        return resp


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    resp = 'image saved'
    if data:
        result = data['image']
        b = bytes(result, 'utf-8')
        image = b[b.find(b'/9'):]
        im = Image.open(io.BytesIO(base64.b64decode(image)))
        im.save('./img.jpeg')
        im.close()

        if(data['sts'] == 'find'):
            resp = facerec(data['home'])

    return resp


@app.route('/message')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
