#!/usr/bin/env python

import rospy
import led
import time
from std_msgs.msg import Float32
from std_msgs.msg import String

def callback(msg):
	pub = rospy.Publisher('talker', String, queue_size=10)
	rospy.loginfo(rospy.get_caller_id() + " I heard: "+ str(msg.data))
	resp=led.traffic(msg.data) #TODO
	pub.publish(resp)

	
def listener_talker():
    rospy.init_node('led_decision', anonymous=True)
    rospy.Subscriber('chatter', Float32, callback)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	try:
		listener_talker()
		
	#when pressing CTR+C	
	except KeyboardInterrupt :
		pass
	print("Measurement stopped by user.")
	
