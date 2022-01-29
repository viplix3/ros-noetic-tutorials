#!/usr/bin/env python
import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String

def talker():
	"""
		Creates a Publisher (talker) rosnode
	"""
	# Publisher object which would be used to publish messages to the topic
	publisher = rospy.Publisher(name='chat_messages', data_class=String, queue_size=20)

	# Initializing the node, the anonymous flag makes sure a unique node is created
	# even if multiple nodes are swapned
	rospy.init_node(name='python_talker', anonymous=True)
	rate = rospy.Rate(hz=1) # Publish speed for messages by the node to the topic

	# Keep publihsing until Ctlr + C is pressed
	iter = 0
	while not rospy.is_shutdown():
		message = "Hello ROS world: %s" % iter
		rospy.loginfo(msg=message)
		publisher.publish(message) # Publish the message to the topic, created rosnode would be used
		rate.sleep()
		iter += 1 # To keep track of different messages

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass