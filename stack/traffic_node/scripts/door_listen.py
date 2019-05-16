#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int8
import openDoor
import closeDoor


def callback(msg):
	rospy.loginfo(rospy.get_caller_id() +" "+ str(msg.data))
	if(msg.data==0):
		openDoor.openDoor()
	elif(msg.data==1):
		closeDoor.closeDoor()
		
def listener():

    rospy.init_node('door_listen', anonymous=True)

    rospy.Subscriber('keypress', Int8, callback)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	try:
		listener()
		
	#when pressing CTR+C	
	except KeyboardInterrupt:
		pass
	p
