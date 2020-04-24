#!/usr/bin/env


from alpha1p import Alpha1P
from time import sleep

# Connect to robot
print("Connecting... ", end="")
robot = Alpha1P()
servo = 0
print("Done")

# Read a single servo
while True:
    print(robot.servo_read(servo))
    sleep(0.3)
