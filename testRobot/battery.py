#!/usr/bin/env


from alpha1p import Alpha1P


# Connect to robot
print("Connecting... ", end="")
robot = Alpha1P()
print("Done")


# Read battery information
print("Battery status:")
print(robot.battery())
