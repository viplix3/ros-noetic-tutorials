#include <iostream>

#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char *argv[]) {

	ros::init(argc, argv, "cpp_talker"); // Initialize the ros node

	ros::NodeHandle ros_node_handle; // Get a handle to the ros node
	ros::Publisher publisher = ros_node_handle.advertise<std_msgs::String>("chat_messages", 20); // Publisher
	ros::Rate loop_rate(1);

	int iter = 0;
	while(ros::ok()) {
		std_msgs::String message;
		std::stringstream ss;
		ss << "Hello ROS world: " << iter;
		message.data = ss.str();

		ROS_INFO("[TALKER_CPP]: %s", message.data.c_str()); // Log the message
		publisher.publish(message); // Publish the message to the topic

		ros::spinOnce();
		loop_rate.sleep();
		iter += 1;
	}

	return 0;
}