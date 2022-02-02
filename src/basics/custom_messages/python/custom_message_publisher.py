#!/usr/bin/env python
import rospy
from rospy.exceptions import ROSInterruptException
from ros_tutorials.msg import IoTSensor
import random

def talker():
	"""
		Creates a Publisher (talker) rosnode
	"""
	# Publisher object which would be used to publish messages to the topic
	publisher = rospy.Publisher(name='IoTSensorData', data_class=IoTSensor, queue_size=20)

	# Initializing the node, the anonymous flag makes sure a unique node is created
	# even if multiple nodes are spawned
	rospy.init_node(name='custom_message_publisher', anonymous=True)
	rate = rospy.Rate(hz=1) # Publish speed for messages by the node to the topic

	# Keep publihsing until Ctlr + C is pressed
	iter = 0
	while not rospy.is_shutdown():
		# IoTSensor() is out custom message class defined inside of msg folder
		custom_message = IoTSensor()
		custom_message.name = "CustomIoTSensor"
		custom_message.id = 69
		custom_message.temperature = 35.6 + random.random()
		custom_message.humidity = 0.15 + random.random()

		rospy.loginfo(msg="Sensor Name: {}  Sensor ID: {}  Temprature: {}  Humidity: {}".format(custom_message.name,
                            custom_message.id, custom_message.temperature, custom_message.humidity))
		publisher.publish(custom_message) # Publish the message to the topic, created rosnode would be used
		rate.sleep()
		iter += 1 # To keep track of different messages

if __name__ == '__main__':
	try:
		talker()
	except ROSInterruptException:
		pass
