import socketio
import random
import string
import json

# standard Python
sio = socketio.Client()

def randomString(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

thisIsATmpTokenListener = randomString(25);

@sio.on(thisIsATmpTokenListener)
def on_message(data):
    if(data['success']):
        print('[+] Successfully registered!')
        addUserKey(data['message'].split(' | ')[1])
        print('[+] Welcome to the Hub!')
        sio.disconnect();
    else:
        print("[-] "+data['message'])

@sio.event
def connect():
    print("[+] Connected to server!")

@sio.event
def connect_error(data):
    print("[-] The connection failed!")

@sio.event
def disconnect():
    print("[-] I'm disconnected, please keep `./user/key.txt` private !")

def addUserKey(userKey):
    f = open("./user/key.txt", "r+")
    f.write(userKey)
    f.close()
    print('[+] User key added!')

def start(username, password):
    sio.connect('http://localhost:8080')
    sio.emit('register', json.dumps({
        "tmp": thisIsATmpTokenListener,
        "username": username,
        "password": password
    }))