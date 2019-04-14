const express = require('express')
const app = express()
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const path = require('path');
const port = 3007
let pisocket = {};
let status = {
    in_progress: false,
    pi_connected: false
};
io.on('connection', socket => {
    socket.emit('conn_received');
    socket.emit('status', status);
    socket.on('pi_connected', () => {
	console.log('pi connected');
        pisocket = socket;
        status.pi_connected = true;
        io.emit('status', status);
        socket.on('pi_finished', () => {
            status.in_progress = false;
            io.emit('status', status);
	    console.log('program finished')        
	});
        socket.on('pi_started', () => {
            status.in_progress = true;
            io.emit('status', status);
            console.log('program started')
	})
        socket.on('disconnect', () => {
	    console.log('pi disconnected')
            status.pi_connected = false;
            io.emit('status', status);
            pisocket = {}
        })
    })
    socket.on('start_prog', () => {
	console.log('attempting to send start request')
        if (pisocket != {}) {
            pisocket.emit("begin");
        } else {
            socket.emit("start_fail");
        }
    })
    socket.on('end_prog', () => {
	console.log('attempting to send end request')
        if (pisocket != {}) {
            pisocket.emit("end");
        }
        else {
            socket.emit("end_fail")
        }
    })
});

app.get('/', (req, res) => {
    //res.send("TEST")
    res.sendFile(path.resolve(__dirname, "public", "index.html"));
});

server.listen(port, () => {
    console.log(`listening on port ${port}`)
})
