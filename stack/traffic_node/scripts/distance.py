#libraries
import RPi.GPIO as GPIO
import time
	
def distance(gpio_echo,gpio_trigger):
	#set Trigger to HIGH
	GPIO.output(gpio_trigger,True)

	#set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(gpio_trigger, False)

	start = time.time()
	stop = time.time()
	#save StartTime
	while GPIO.input(gpio_echo)==0:
		start == time.time()

	#save time of arrival
	while GPIO.input(gpio_echo)==1:
		stop= time.time()

	#time difference between start and arrival
	timeElapsed = stop-start

	#multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
	distance = (timeElapsed*34300)/2

	return distance




