const sio = io('ws://localhost:8000', {
  transports: ['websocket'],
  secure: false,
  rejectUnauthorized: false,
  upgrade: false,
  reconnectionDelayMax: 10000,
  path: '/ws'
});

sio.on('connect', () => {
  console.log('connected');
});

sio.on('disconnect', () => {
  console.log('disconnected');
});