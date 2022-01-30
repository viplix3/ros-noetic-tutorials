#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose as turtlesim_pose


def poseCallback(pose_message):

	rospy.loginfo("Position (x, y, theta): ({}, {}, {})".format(pose_message.x, pose_message.y, pose_message.theta))

def turtle_pose_info():
	rospy.init_node('turtlesim_motion_pose', anonymous=True)        
	rospy.Subscriber(name='turtle1/pose', data_class=turtlesim_pose, callback=poseCallback)

	rospy.spin()

if __name__ == '__main__':
	try:
		turtle_pose_info()
	except rospy.ROSInterruptException:
		rospy.loginfo("node terminated.")