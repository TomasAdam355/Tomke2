Hello world

array_publisher.py:
#!/usr/bin/env python

import numpy
import rospy
from std_msgs.msg import Int64

def array_publish():
    pub = rospy.Publisher('mytopic', Int64, queue_size=10)
    rospy.init_node('new_talker', anonymous=True)
    MyArray = numpy.array([3,5,9,1,6])
    pub.publish(MyArray)

if __name__ == '__main__':
    array_publish()
