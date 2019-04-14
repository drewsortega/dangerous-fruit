import RPi.GPIO as GPIO
import time 
import sys

out1 = 13
out2 = 11
out3 = 15
out4 = 12

i=0
positive=0
negative=0
y=0

speed=0.007

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)



try:
   while(1):
       for i in range(0,8):
          if i==0:
              GPIO.output(out1,GPIO.HIGH)
              GPIO.output(out2,GPIO.LOW)
              GPIO.output(out3,GPIO.LOW)
              GPIO.output(out4,GPIO.LOW)
              time.sleep(speed)
              #time.sleep(1)
          elif i==1:
              GPIO.output(out1,GPIO.HIGH)
              GPIO.output(out2,GPIO.HIGH)
              GPIO.output(out3,GPIO.LOW)
              GPIO.output(out4,GPIO.LOW)
              time.sleep(speed)
              #time.sleep(1)
          elif i==2:  
              GPIO.output(out1,GPIO.LOW)
              GPIO.output(out2,GPIO.HIGH)
              GPIO.output(out3,GPIO.LOW)
              GPIO.output(out4,GPIO.LOW)
              time.sleep(speed)
              #time.sleep(1)
          elif i==3:    
              GPIO.output(out1,GPIO.LOW)
              GPIO.output(out2,GPIO.HIGH)
              GPIO.output(out3,GPIO.HIGH)
              GPIO.output(out4,GPIO.LOW)
              time.sleep(speed)
              #time.sleep(1)
          elif i==4:  
              GPIO.output(out1,GPIO.LOW)
              GPIO.output(out2,GPIO.LOW)
              GPIO.output(out3,GPIO.HIGH)
              GPIO.output(out4,GPIO.LOW)
              time.sleep(speed)
              #time.sleep(1)
          elif i==5:
              GPIO.output(out1,GPIO.LOW)
              GPIO.output(out2,GPIO.LOW)
              GPIO.output(out3,GPIO.HIGH)
              GPIO.output(out4,GPIO.HIGH)
              time.sleep(speed)
              #time.sleep(1)
          elif i==6:    
              GPIO.output(out1,GPIO.LOW)
              GPIO.output(out2,GPIO.LOW)
              GPIO.output(out3,GPIO.LOW)
              GPIO.output(out4,GPIO.HIGH)
              time.sleep(speed)
              #time.sleep(1)
          elif i==7:    
              GPIO.output(out1,GPIO.HIGH)
              GPIO.output(out2,GPIO.LOW)
              GPIO.output(out3,GPIO.LOW)
              GPIO.output(out4,GPIO.HIGH)
              time.sleep(speed)
              #time.sleep(1)
  
  
             
except KeyboardInterrupt:
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    GPIO.cleanup()
