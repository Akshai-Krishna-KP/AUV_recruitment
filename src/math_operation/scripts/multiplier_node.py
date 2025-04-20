#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    multiplied = msg.data * 10
    rospy.loginfo(f"Received {msg.data}, publidhing {multiplied}")
    pub.publish(multiplied)

if __name__ == "__main__":
    rospy.init_node("multiplier_node")
    rospy.loginfo("Multiply the recieved value by 10")

    pub = rospy.Publisher("/times_10", Int32, queue_size=10)

    sub = rospy.Subscriber("/multiples_of_2", Int32, callback)

    rospy.spin()