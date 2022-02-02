#include "ros/ros.h"
#include "std_msgs/String.h"

void chatter_callback(const std_msgs::String::ConstPtr& msgs) {
	ROS_INFO("[LISTENER_CPP] heard data \"%s\"", msgs->data.c_str());
}

int main(int argc, char *argv[]) {

	ros::init(argc, argv, "cpp_listener"); // Initialize ros node

	ros::NodeHandle node_handle; // Get a handle to the ros node
	ros::Subscriber subscriber = node_handle.subscribe("chat_messages", 20, chatter_callback);
	ros::spin();

	return 0;
}