#!/usr/bin/env python3
import rospy
import subprocess
if __name__ == '__main__':
    rospy.init_node('lab1_launch', anonymous=True)
    package_name = 'lab_1_pkg'
    talker_node = 'talker.py'
    relay_node = 'relay.py'
    talker_process = subprocess.Popen(['rosrun', package_name, talker_node])
    relay_process = subprocess.Popen(['rosrun', package_name, relay_node])
    rospy.loginfo("Nodes launched.")
    talker_process.wait()
    relay_process.wait()