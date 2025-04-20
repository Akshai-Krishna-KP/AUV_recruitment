#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node("Publish multiple of two")
    rospy.loginfo("Two Multiplier sending node has started")

    pub = rospy.Publisher("/multiples_of_2", Int32, queue_size=10)

    rate = rospy.Rate(1)
    count  = 1

    while not rospy.is_shutdown():
        number = 2 * count
        rospy.loginfo(f"Publish: {number}")
        pub.publish(number)
        count += 1
        rate.sleep()