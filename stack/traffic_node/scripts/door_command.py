#!/usr/bin/env python

import rospy
import distance
from std_msgs.msg import Int8

def talker():
	
    pub = rospy.Publisher('keypress_door', Int8, queue_size=10)
    rospy.init_node('door_command', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():	
		print("Press 1 to open or 0 for close and then enter. ")	
		n = int(raw_input())	
		rospy.loginfo(str(n))
		pub.publish(n)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		rospy.loginfo("Measurement stopped by user.")

