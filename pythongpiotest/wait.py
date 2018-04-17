import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

channel = GPIO.wait_for_edge(3, GPIO_RISING)
if channel is None:
	print('Timeout occured')
else:
	print('Edge detected on channel', channel)

GPIO.cleanup()
