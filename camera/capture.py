from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.start_preview()
camera.annotate_text = "Tallulah"
# Camera warm-up time
sleep(2)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
