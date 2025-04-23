import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led1 = 15
gpio.setup(led1,gpio.OUT,initial=1)

file1 = open('led.txt','r')
lines = file1.readlines()

ON_TIME = int(lines[0].split("=")[1])
OFF_TIME = int(lines[1].split("=")[1])

try:
    while(True):
        gpio.output(led1,False)
        time.sleep(ON_TIME)
        gpio.output(led1,True)
        time.sleep(OFF_TIME)
except KeyboardInterrupt:
    gpio.cleanup()
