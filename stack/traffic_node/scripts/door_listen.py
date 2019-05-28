#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
import openDoor
import closeDoor
import RPi.GPIO as GPIO

def callback(msg):
	pwm = GPIO.PWM(21, 50)
	rospy.loginfo(rospy.get_caller_id() +" "+ str(msg.data))
	if(msg.data==0):
		openDoor.openDoor(pwm)
	elif(msg.data==1):
		closeDoor.closeDoor(pwm)
		
def listener():

	rospy.init_node('door_listen', anonymous=True)

	rospy.Subscriber('keypress_door', Int8, callback)

 	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(21, GPIO.OUT)
    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
		GPIO.cleanup()
		
	#when pressing CTR+C	
	except KeyboardInterrupt:
		pass
	
