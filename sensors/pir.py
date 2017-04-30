#!/usr/bin/env python
import time 
import RPi.GPIO as io
from gpiozero import Buzzer
io.setmode(io.BCM)
buzzer = Buzzer(26)
pir_pin = 24 
red_led_pin = 20
green_led_pin = 21

def setup():
  print("Initializing ... ")
  io.setup(pir_pin, io.IN) 
  io.setup(red_led_pin, io.OUT)
  io.setup(green_led_pin, io.OUT)
  io.output(red_led_pin, False)
  io.output(green_led_pin, True)
 
def process():
    if io.input(pir_pin):
       print("Intruder detected .. ")
       buzzer.beep()
       io.output(red_led_pin, True)
       io.output(green_led_pin, False)
       time.sleep(5);
       print("You are Safe !")
       buzzer.off()
       io.output(red_led_pin, False)
       io.output(green_led_pin, True)
       time.sleep(5)
    time.sleep(1)
def destroy():
    print("Cleaning up...")
    io.cleanup(red_led_pin) # Release Resource
    io.cleanup(pir_pin)
    io.cleanup(green_led_pin)
# Program starts from here ..
if __name__ == '__main__': 
    print 'Press Ctrl+C to end the program...'
    try:
       setup()
       while True:
          process()
    except KeyboardInterrupt:  
      # here you put any code you want to run before the program   
      # exits when you press CTRL+C  
      print "\nExiting..."  
      destroy()  
    except:  
      # this catches ALL other exceptions including errors.  
      # You won't get any error messages for debugging  
      # so only use it once your code is working  
      print "Other error or exception occurred!"  
    finally:
      print "finally block"
