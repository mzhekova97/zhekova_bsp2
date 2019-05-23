import RPi.GPIO as GPIO
import time

def traffic(dist,ledRed,ledYellow,ledGreen):
	mess = ""
	#RED
	if(dist<=20.0):
		mess="--STOP!  The distance is "+str(dist)+ " It is red. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledRed,GPIO.HIGH)

	#YELLOW
	if(dist>20.0 and dist<=40.0):
		mess="--ATTENTION!  The distance is "+str(dist)+ " It is yellow. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledYellow,GPIO.HIGH)

	#GREEN
	if(dist>40.0):
		mess="--You may proceed!  The distance is "+str(dist)+" It is green. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledGreen,GPIO.HIGH)


	return mess
	
	
