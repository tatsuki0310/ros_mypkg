#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('send')
pub = rospy.Publisher('new_send', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    n = random.randrange(100000)
    pub.publish(n)
    print(n)
    rate.sleep()
