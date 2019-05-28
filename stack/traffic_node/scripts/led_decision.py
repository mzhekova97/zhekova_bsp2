#!/usr/bin/env python

import rospy
import led
from std_msgs.msg import Float32
from std_msgs.msg import String
import RPi.GPIO as GPIO

ledRed = 17
ledYellow = 18
ledGreen = 22

def callback(msg):
	pub = rospy.Publisher('color_of_led', String, queue_size=10)
	rospy.loginfo(rospy.get_caller_id() + " I heard: "+ str(msg.data))
	resp=led.traffic(msg.data,ledRed,ledYellow,ledGreen) 
	pub.publish(resp)


def listener_talker():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	GPIO.setup(ledRed, GPIO.OUT) 
	GPIO.setup(ledYellow, GPIO.OUT) 
	GPIO.setup(ledGreen, GPIO.OUT)
	
	rospy.init_node('led_decision', anonymous=True)
	rospy.Subscriber('distance_from_sensor', Float32, callback)
    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		listener_talker()
		GPIO.cleanup()
		
	#when pressing CTR+C	
	except KeyboardInterrupt :
		pass
	print("Measurement stopped by user.")
	
