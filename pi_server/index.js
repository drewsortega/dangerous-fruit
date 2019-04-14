let io = require('socket.io-client')
const util = require('util')
const spawn = require('child_process').spawn;
const path = require('path')
let process = {};
let running = false;

socket = io.connect("http://flip1.engr.oregonstate.edu:3008");
socket.on("conn_received", () => {
    console.log('connected to server');
    socket.emit("pi_connected");
})
socket.on("begin", () => {
    console.log('beginning program');
    if (!running) {
        process = spawn('python', [path.resolve(__dirname, 'fruit_ninja.py')])
        running = true;
    }
})
socket.on("end", () => {
    console.log('ending program');
    if (running) {
        kill(child.pid, 'SIGINT');
        running = false;
    }
})