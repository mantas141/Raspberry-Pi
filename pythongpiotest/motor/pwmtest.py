import RPi.GPIO as GPIO
import time

PWMA = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)

rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
rightmotor.start(0)

rightmotor.ChangeDutyCycle(20)
time.sleep(2)

rightmotor.ChangeDutyCycle(40)
time.sleep(2)

rightmotor.ChangeDutyCycle(60)
time.sleep(2)

rightmotor.ChangeDutyCycle(80)
time.sleep(2)

rightmotor.ChangeDutyCycle(100)
time.sleep(2)

rightmotor.ChangeDutyCycle(0)

GPIO.cleanup()
time.sleep(0.01)
print " Cleaned up pins"
