#!/usr/bin/env python3
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
def callback(data):
    new_msg=AckermannDriveStamped()
    new_msg.drive.speed=data.drive.speed*3
    new_msg.drive.steering_angle=data.drive.steering_angle*3
    pub.publish(new_msg)
def relay():
    rospy.init_node('relay', anonymous=True)
    rospy.Subscriber('drive', AckermannDriveStamped, callback)
    global pub
    pub = rospy.Publisher('drive_relay', AckermannDriveStamped, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        relay()
    except rospy.ROSInterruptException:
        pass
