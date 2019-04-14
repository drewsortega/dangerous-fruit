let io = require('socket.io-client')
const util = require('util')
const spawn = require('child_process').spawn;
const path = require('path')
let process = {};
let running = false;
console.log('starting local pi server')
socket = io.connect("http://flip1.engr.oregonstate.edu:3007");
socket.on("conn_received", () => {
    console.log('connected to server');
    socket.emit("pi_connected");
})
socket.on("begin", () => {
    if (!running) {
        console.log('beginning program');
        process = spawn('python', [path.resolve(__dirname, 'src', 'fruit_ninja.py')])
        running = true;
        process.on('exit', function () {
            console.log('process finished');
            running = false;
            socket.emit("pi_finished")
        })
        socket.emit("pi_started")
    } else {
        console.log('attempted to start when already running')
    }
})
socket.on("end", () => {
    if (running) {
        console.log('ending program');
        process.kill();
    } else {
        console.log('attempted to end when not running');
    }
})
