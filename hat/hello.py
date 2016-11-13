from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_pixel(0,2,[0,0,255])
sense.set_pixel(7,4,[255,0,0])
sleep(1)
r = randint(0,255)
sense.show_letter("T", text_colour=[0,r,0])
sleep(2)
sense.show_message("Hello Dad, I'm tallulah", scroll_speed=0.12, text_colour=[0,251,0], back_colour=[0,0,0])

sense.clear()
