#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys
import select

user_name = ""
pub = None

def receive_messages(msg):
    """ Callback to receive and display all messages """
    print(f"\n{msg.data}")

def check_user_input(event):
    """ Timer callback to check if user typed anything (non-blocking) """
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        msg = sys.stdin.readline().strip()
        if msg:
            pub.publish(f"{user_name}: {msg}")

def main():
    global user_name, pub

    if len(sys.argv) < 2:
        print("Usage: rosrun chat_package chat_node.py <YourName>")
        return

    user_name = sys.argv[1]

    rospy.init_node("chat_node_" + user_name, anonymous=True)
    pub = rospy.Publisher("/chat_topic", String, queue_size=10)
    rospy.Subscriber("/chat_topic", String, receive_messages)

    rospy.Timer(rospy.Duration(0.1), check_user_input)

    rospy.loginfo(f"[{user_name}] Chat node started. Type your message below:")
    rospy.spin()

if __name__ == "__main__":
    main()
