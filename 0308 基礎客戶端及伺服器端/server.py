import uvicorn
from fastapi import FastAPI, WebSocket
import socketio

app = FastAPI()

sio = socketio.AsyncServer(async_mode = 'asgi')

@sio.event
async def connect(sid, env, a):
    print(f'{sid} joined!')

@sio.on('disconnect')
async def disconnect(sid):
    print(f'{sid} disconnected!')

@sio.event
async def message(sid, message):
    print(f'{sid} says :{message}.')
    data = {
        'uid' : sid,
        'message' : message
    }
    await sio.emit('message', data, skip_sid = sid)




sio_asgi_app = socketio.ASGIApp(sio, app)

app.mount('/', sio_asgi_app)


if __name__ == "__main__":    
    uvicorn.run("server:app", host = "0.0.0.0", port = 8000, reload = True)