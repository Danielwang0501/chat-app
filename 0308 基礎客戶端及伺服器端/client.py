import socketio

ci = socketio.Client()

@ci.on("connect")
def connect():
    print('connected')

@ci.on('message')
def message(data):
    print(f"{data['uid']} said :{data['message']}")

ci.connect('ws://192.168.1.118:8000')

while True:
    message = input()
    ci.emit('message', message)