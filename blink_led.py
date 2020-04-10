
import RPi.GPIO as gpio
import time 

def set_pwm_dc(pwm,dc):
    pwm.ChangeDutyCycle(dc)
    return pwm
    
def set_pwm_f(pwm,f):
    p.ChangeFrequency(f)
    return pwm

def ptest():
    print('hello')

def my_callback(channel):
    if gpio.input(32):
      set_pwm_dc(p,50)
    else:
      set_pwm_dc(p,100)

#set board    
gpio.setmode(gpio.BOARD)

#set gpio 36
gpio.setup(36,gpio.OUT)
p = gpio.PWM(36,0.5)
p.start(50)

#set gio 32, with event detect
gpio.setup(32,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.add_event_detect(32, gpio.BOTH, callback=my_callback)


    





