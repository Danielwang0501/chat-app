import socketio

ci = socketio.Client()

@ci.on("connect")
def connect():
    print('connected')

@ci.on('message')
def message(data):
    print(f"{data['uid']} said :{data['message']}")

ci.connect('ws://127.1:8000')

while True:
    message = input()
    ci.emit('message', message)
