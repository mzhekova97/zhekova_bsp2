#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + msg.data)
	
		
def listener():

    rospy.init_node('led_visualisation', anonymous=True)

    rospy.Subscriber('talker', String, callback)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	try:
		listener()
		
	#when pressing CTR+C	
	except KeyboardInterrupt:
		pass
	print("Measurement stopped by user.")
	
