import RPi.GPIO as GPIO
import time
#import distance



def traffic(dist):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	ledRed = 17
	ledYellow = 18
	ledGreen = 22
	mess = ""

	GPIO.setup(ledRed, GPIO.OUT) 
	GPIO.setup(ledYellow, GPIO.OUT) 
	GPIO.setup(ledGreen, GPIO.OUT)
	#RED
	if(dist<=20.0):
		mess="STOP!  The distance is "+str(dist)+ " It is red. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledRed,GPIO.HIGH)
		GPIO.cleanup()
	#YELLOW
	if(dist>20.0 and dist<=40.0):
		mess="ATTENTION!  The distance is "+str(dist)+ " It is yellow. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledYellow,GPIO.HIGH)
		GPIO.cleanup()
	#GREEN
	if(dist>40.0):
		mess="You may proceed!  The distance is "+str(dist)+" It is green. "
		GPIO.output(ledRed,GPIO.LOW)
		GPIO.output(ledYellow,GPIO.LOW)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(0.0001) 
		GPIO.output(ledGreen,GPIO.HIGH)
		GPIO.cleanup()

	return mess
	
	
