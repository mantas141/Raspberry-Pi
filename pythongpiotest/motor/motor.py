import RPi.GPIO as GPIO
import time

PWMA = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)

rightmotor = GPIO.PWM(PWMA, 50)
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

rightmotor.ChangeDutyCycle(80)
time.sleep(0.5)

rightmotor.ChangeDutyCycle(60)
time.sleep(0.5)

rightmotor.ChangeDutyCycle(40)
time.sleep(0.5)

rightmotor.ChangeDutyCycle(20)
time.sleep(0.5)

rightmotor.ChangeDutyCycle(0)

time.sleep(2)

GPIO.output(17, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)

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
print "Pins cleaned up"