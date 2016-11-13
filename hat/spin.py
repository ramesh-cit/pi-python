from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.show_letter("A")
angles = [0,90,180,270,0,90,180,270]
for r in angles:
   sense.set_rotation(r)
   sleep(0.5)
sense.clear()
