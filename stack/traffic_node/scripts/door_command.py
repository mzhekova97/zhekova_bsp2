#!/usr/bin/env python

import rospy
import distance
from std_msgs.msg import Int8
from std_msgs.msg import String
import time

def talker():
    pub = rospy.Publisher('keypress', Int8, queue_size=10)
    rospy.init_node('door_command', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():	
		print("Press 1 to open or 0 for close and then enter. ")
		#k=ord(getch.getch()) #to convert keypress event
		n = int(raw_input())
		#if ((k>=65)&(k<=68)|(k==115)|(k==113)|(k==97)):	
		rospy.loginfo(str(n))
		pub.publish(n)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		rospy.loginfo("Measurement stopped by user.")
    #except rospy.ROSInterruptException:
	#rospy.loginfo("Measurement stopped by user.")
	#GPIO.cleanup()
