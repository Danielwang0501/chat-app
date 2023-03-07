from server import app

@app.sio.on('message')
async def handle_join(sid, data):
    print(f"Received message from {sid}: {data}")
    await app.sio.emit("message", f"Hello, {sid}!")

