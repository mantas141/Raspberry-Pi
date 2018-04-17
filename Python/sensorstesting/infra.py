import RPi.GPIO as GPIO
import time
IRsensor1 = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRsensor1, GPIO.IN)

while True:
	A = GPIO.input(IRsensor1)
	print (A)
	time.sleep(0.01)
