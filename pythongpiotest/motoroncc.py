import RPi.GPIO as GPIO
import time

PWMA = 27

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)


GPIO.output(17, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)

rightmotor = GPIO.PWM(PWMA, 50)
rightmotor.start(0)

rightmotor.ChangeDutyCycle(100)
