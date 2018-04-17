import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
	while True:
		GPIO.output(17, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
	
except KeyboardInterrupt:
	GPIO.cleanup()
	time.sleep(0.01)
print " Cleaned up pins"