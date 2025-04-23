import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
led1=15
led2=13
switch1=37
switch2=35
gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(led2,gpio.OUT,initial=1)
gpio.setup(switch1,gpio.IN)
gpio.setup(switch2,gpio.IN)

def glow_led(event):
    if event==switch1:
        gpio.output(led1,False)
        time.sleep(3)
        gpio.output(led1,True)
    elif event==switch2:
        gpio.output(led2,False)
        time.sleep(3)
        gpio.output(led2,True)
        
gpio.add_event_detect(switch1,gpio.RISING,callback=glow_led,bouncetime=1)
gpio.add_event_detect(switch2,gpio.RISING,callback=glow_led,bouncetime=1)
try:
    while(True):
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()
        
        
    
