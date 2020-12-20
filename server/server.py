import json
import random
import string
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from pprint import pprint
from dataManager import DataManager

app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '4200'

@app.route('/index.html')
def home():
    """
    Summary: serves index.html file to clients connecting on the home page
    """

    return render_template('index.html')

@app.route('/create.html')
def create():
    """
    Summary: serves create.html file to clients creating an event
    """

    return render_template('create.html')

@app.route('/get-images', methods=['GET'])
def getImages():
    """
    Summary: returns image urls for a given event code
    """

    eventCode = request.args.get('eventcode')
    images = dbManager.getEventImages(eventCode)
    return json.dumps(images)

def generateCode():
    """
    Summary: generates a unique three letter code for a new event
    """

    letters = string.ascii_lowercase
    code = ''
    unique = False
    while not unique:
        for i in range(3):
            code += letters[random.randint(0,25)]
        unique = dbManager.testCode(code)
    print("Generated event code:", code)
    return code

def parseURL(inp):
    """
    Summary: parses list of urls submitted in frontend
    """

    urls = []
    for url in inp.split(", "):
        urls.append(url)
    return urls

@app.route('/create-event', methods=['POST'])
def createEvent():
    """
    Summary: endpoint for creating a new event
    """
    
    code = generateCode()
    payload = request.get_data().decode('utf-8')
    payload = json.loads(payload)

    payload["images"] = parseURL(payload["urlList"])
    

    if payload["code"] == "abc":
        code = "abc"
        payload["images"] = []

    payload['code'] = code
    pprint(payload)
    dbManager.addEvent(payload)
    response = {'code': code}
    return json.dumps(response)

if __name__ == '__main__':
    dbManager = DataManager()
    app.run(host=HOST, port=PORT)