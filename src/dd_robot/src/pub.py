# let's create a publisher node
# we are using std_msgs.msg String
# we are publishing to the topic "chatter_1"
# we are publishing 10 times a second
# we are publishing the message "Hello World"

import rospy
import time
import std_msgs.msg

if __name__ == '__main__':
    rospy.init_node('publisher_node')
    pub = rospy.Publisher('chatter_1', std_msgs.msg.String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish("Hello World")
        rate.sleep()

# Path: src/dd_robot/src/sub.py