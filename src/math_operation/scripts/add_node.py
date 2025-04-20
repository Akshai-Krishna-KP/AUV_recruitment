#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    result = msg.data + 5
    rospy.loginfo(f"Received {msg.data}, final result: {result}")

if __name__ == "__main__":
    rospy.init_node("adder_node")
    rospy.loginfo("Adder node has started")

    sub = rospy.Subscriber("/times_10", Int32, callback)

    rospy.spin()