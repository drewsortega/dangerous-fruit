import RPi.GPIO as GPIO
import time
import sys
import signal
import wheels
import arm
import random

out_vdd = 12
out_gnd = 11
out_w1 = 29
out_w2 = 31
out_w3 = 32
out_w4 = 33

chance_turn = 5

max_time = 20
cur_time = 0

left_rotate_time = 0
right_rotate_time = 50
cur_rotate_time = 25

GPIO.setmode(GPIO.BOARD)

def sigterm_handler(signal, frame):
        print('quitting')
        GPIO.output(out_vdd, GPIO.LOW)
        GPIO.output(out_gnd, GPIO.LOW)
        GPIO.output(out_w1, GPIO.LOW)
        GPIO.output(out_w2, GPIO.LOW)
        GPIO.output(out_w3, GPIO.LOW)
        GPIO.output(out_w4, GPIO.LOW)
        GPIO.cleanup()

signal.signal(signal.SIGTERM, sigterm_handler)
try:
    arm.start()
    while(cur_time<max_time):
        time.sleep(1)
        cur_time += 1
        if(random.randint(1, chance_turn) == 1):
            # turn
            if(random.randint(1, 2) == 1 and cur_rotate_time < right_rotate_time):
                add_rotate_time = min(random.randint(1, 4), right_rotate_time-cur_rotate_time)
                wheels.forward(add_rotate_time)
                cur_rotate_time += add_rotate_time
                cur_time += add_rotate_time
            else:
                rem_rotate_time = min(random.randint(1, 4), cur_rotate_time-left_rotate_time)
                wheels.backward(rem_rotate_time)
                cur_rotate_time -= rem_rotate_time
                cur_time += rem_rotate_time
    arm.end()

except KeyboardInterrupt:
        print('quitting')
        GPIO.output(out_vdd, GPIO.LOW)
        GPIO.output(out_gnd, GPIO.LOW)
        GPIO.output(out_w1, GPIO.LOW)
        GPIO.output(out_w2, GPIO.LOW)
        GPIO.output(out_w3, GPIO.LOW)
        GPIO.output(out_w4, GPIO.LOW)
        GPIO.cleanup()
