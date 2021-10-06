#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

class Turtlebot():
    def __init__(self):
        rospy.init_node("turtlebot_move")
        rospy.loginfo("Press Ctrl + C to terminate")
        self.vel_pub = rospy.Publisher("cmd_vel_mux/input/navi", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.run()


    def run(self):
        turning_range = 34
        #35 30 33(worked well)
        forward_range =  78
        #100(too far) 80(close) 81 82 83(little too far)
        vel = Twist()
        #goes forward
        vel.linear.x = 0.5
        vel.angular.z = 0
        #while not rospy.is_shutdown():  # uncomment to use while loop
        for i in range(forward_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()
        
        #turns left
        vel.linear.x = 0
        vel.angular.z = 0.5
        for i in range(turning_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()
        
        #goes forward
        vel.linear.x = 0.5
        vel.angular.z = 0
        #while not rospy.is_shutdown():  # uncomment to use while loop
        for i in range(forward_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()
        
        #turns left
        vel.linear.x = 0
        vel.angular.z = 0.5
        for i in range(turning_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()


        #goes forward
        vel.linear.x = 0.5
        vel.angular.z = 0
        #while not rospy.is_shutdown():  # uncomment to use while loop
        for i in range(forward_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()

        #turns left
        vel.linear.x = 0
        vel.angular.z = 0.5
        for i in range(turning_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()

        #goes forward
        vel.linear.x = 0.5
        vel.angular.z = 0
        #while not rospy.is_shutdown():  # uncomment to use while loop
        for i in range(forward_range):
            self.vel_pub.publish(vel)
            self.rate.sleep()




        
        
        
        
        


if __name__ == '__main__':
    try:
        whatever = Turtlebot()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action terminated.")
