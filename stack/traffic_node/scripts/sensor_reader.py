#!/usr/bin/env python

import rospy
import distance
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

def talker():
	GPIO.setwarnings(False)
	#GPIO Mode --> BCM
	GPIO.setmode(GPIO.BCM)

	#set GPIO Pins
	gpio_trigger = 4 
	gpio_echo = 27

	#set GPIO direction (IN/OUT)
	GPIO.setup(gpio_trigger, GPIO.OUT)
	GPIO.setup(gpio_echo, GPIO.IN)

	pub = rospy.Publisher('distance_from_sensor', Float32, queue_size=10)
	rospy.init_node('sensor_reader', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	while not rospy.is_shutdown():
		dist = distance.distance(gpio_echo,gpio_trigger)
		rospy.loginfo(dist)
		pub.publish(dist)
		rate.sleep()
	GPIO.cleanup()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
	rospy.loginfo("Measurement stopped by user.")

        
