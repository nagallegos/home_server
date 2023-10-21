import RPi.GPIO as rpi
import time


led1,led2,led3= 11,13,15

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(led1, rpi.OUT)
rpi.setup(led2, rpi.OUT)
rpi.setup(led3, rpi.OUT)
rpi.output(led1, 0)
rpi.output(led2, 0)
rpi.output(led3, 0)
print("Done")

def blink1(led):
    count = 0
    sleep_time = .05
    while(count < 4):
        rpi.output(led,1)
        time.sleep(sleep_time)
        rpi.output(led,0)
        time.sleep(sleep_time)
        count = count + 1