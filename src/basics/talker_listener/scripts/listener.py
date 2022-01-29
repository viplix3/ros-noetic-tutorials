#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def listener_classback(message):
	"""
		This is the function caleed by Subscriber (listener) node whenever it reads \
		a message from a relevant topic
	"""
	rospy.loginfo(rospy.get_caller_id() + "Listener heard %s" % message)

def listener():
	"""
		Created a Subscriber (listener) rosnode
	"""
	# Initializing the node, the anonymous flag makes sure a unique node is created
	# even if multiple nodes are swapned
	rospy.init_node(name='python_listener', anonymous=True)
	rospy.Subscriber(name='chat_messages', data_class=String, callback=listener_classback)

	# spin() makes sure node will keep on running until stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass