import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.out)
count = input("How many times you want it to blink?: ")
while count > 0:
	GPIO.output(3,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(3,GPIO.LOW)
	time.sleep(1)
	count = count - 1
GPIO.cleanup()
