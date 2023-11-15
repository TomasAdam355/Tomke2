#!/usr/bin/env python

import rospy
from factor.srv import factor, factorResponse
import numpy

def callback(request):
	return factorResponse(numpy.math.factorial(request.a))

def multiply():
	rospy.init_node("new_server")
	s = rospy.Service('factor', factor, callback)
	rospy.spin()


if __name__ == '__main__':
	multiply()
	
	array_subscriber.py:
#!/usr/bin/env python

import rospy
import numpy
from std_msgs.msg import Int16

def callback(data):
    print(numpy.mean(data))
    
def array_subscribe():
	rospy.init_node('array_subscriber', anonymous=True)
	rospy.Subscriber('mytopic', Int16, callback)

if __name__ == '__main__':
	array_subscribe()

