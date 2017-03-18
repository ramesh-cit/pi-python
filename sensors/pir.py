import time 
from gpiozero import Buzzer
buzzer = Buzzer(26)

import RPi.GPIO as io 
io.setmode(io.BCM) 
 
pir_pin = 24 
red_led_pin = 20
green_led_pin = 21
 
io.setup(pir_pin, io.IN) 
io.setup(red_led_pin, io.OUT)
io.setup(green_led_pin, io.OUT)
io.output(red_led_pin, False)
io.output(green_led_pin, True)
 


while True:
    if io.input(pir_pin):
        print("POWER ON")
        buzzer.beep()
        io.output(red_led_pin, True)
        io.output(green_led_pin, False)
        time.sleep(5);
        print("POWER OFF")
        buzzer.off()
        io.output(red_led_pin, False)
        io.output(green_led_pin, True)
        time.sleep(5)
    time.sleep(1)
