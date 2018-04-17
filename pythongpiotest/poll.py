import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while GPIO.input(4)== GPIO.LOW:
	time.sleep(0.1)

if GPIO.input(4):
	print('Input was HIGH')
else:
	print('Input was LOW')


GPIO.cleanup()
