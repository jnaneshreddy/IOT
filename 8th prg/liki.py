import time
import RPi.GPIO as gpio
from flask import Flask,render_template
import datetime
app=Flask(__name__)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
led1=13
switch1=35
gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(switch1,gpio.IN)
light_status="ON"
def glow_led(event):
    print("Entered Here")
    global light_status
    if event==switch1 and light_status=="OFF":
        gpio.output(led1,False)
        light_status="ON"
    elif event==switch1 and light_status=="ON":
         gpio.output(led1,True)
         light_status="OFF"
@app.route('/')
def ledstatus():
    now=datetime.datetime.now()
    timeString=now.strftime("%H:%M %d-%m-%Y")
    templateDate={
    'status': light_status,
    'time': timeString
    }
    return render_template('lightstatus.html',**templateDate)
gpio.add_event_detect(switch1,gpio.RISING,callback=glow_led,bouncetime=100)
app.run(debug=True,port=3001,host='127.0.0.1')

                           