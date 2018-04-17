import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

while True:
	GPIO.output(4, GPIO.input(3))
	print (GPIO.input(3))
	time.sleep
	
GPIO.cleanup()