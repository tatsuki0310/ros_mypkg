#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(msg):
    global n
    if msg.data % 2 == 0:
        print(msg.data, ': even')
    else :
        print(msg.data, ': odd')

if __name__=='__main__':
    rospy.init_node('return')
    sub = rospy.Subscriber('new_send', Int32, cb)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
