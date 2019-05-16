#!/usr/bin/env python

import rospy
import distance
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time

def talker():
    pub = rospy.Publisher('chatter', Float32, queue_size=10)
    rospy.init_node('sensor_reader', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        dist = distance.distance()
        rospy.loginfo(dist)
        pub.publish(dist)
        rate.sleep()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
	rospy.loginfo("Measurement stopped by user.")
	GPIO.cleanup()
        
