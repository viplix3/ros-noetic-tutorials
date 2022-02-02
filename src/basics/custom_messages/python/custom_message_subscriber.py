#!/usr/bin/env python
import rospy
from ros_tutorials.msg import IoTSensor

def listener_classback(custom_message):
	"""
		This is the function caleed by Subscriber (listener) node whenever it reads \
		a message from a relevant topic
	"""
	rospy.loginfo(rospy.get_caller_id() + "\tSensor Name: {}  Sensor ID: {}  Temprature: {}  Humidity: {}".format(custom_message.name,
						custom_message.id, custom_message.temperature, custom_message.humidity))

def listener():
	"""
		Created a Subscriber (listener) rosnode
	"""
	# Initializing the node, the anonymous flag makes sure a unique node is created
	# even if multiple nodes are spawned
	rospy.init_node(name='custom_message_subscriber', anonymous=True)
	rospy.Subscriber(name='IoTSensorData', data_class=IoTSensor, callback=listener_classback)

	# spin() makes sure node will keep on running until stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
