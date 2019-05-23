import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle,pwm):

	pwm.start(0)
	
	duty = angle /18+2
	GPIO.output(21, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(21,False)
	pwm.ChangeDutyCycle(0)
	pwm.stop()


