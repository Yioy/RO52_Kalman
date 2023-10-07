#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys
from motorControl import MotorControl
from colorSensorControl import ColorSensorControl
from distanceSensorControl import DistanceSensorControl
from kalman import Kalman
from gyroscope import Gyroscope
from command import Command
from leader import Leader
from suiveur import Suiveur
from log import clear_log
from log import write_log
import time
import math

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

print("sys.version")

# Write your program here.

# Initialisation
motorController = MotorControl(Port.B, Port.C)
colorController = ColorSensorControl(Port.S3)
distanceController = DistanceSensorControl(Port.S2)
robot = DriveBase(Motor(Port.B), Motor(Port.C), 56, 114)
command = Command(0.4, 1, 0.1, 0.1, 150, 150)
kalman = Kalman((math.pi*10/180), 5, 1.5, 0, 5)

old_angle = 0
old_distance_state = 0
distance_state = 0

speed = 100
angular_speed = 0
angle = 0
x = 0
y = 0

gyroscope = Gyroscope(Port.S4, speed)

timestamp = time.time()
elapsed_time = 0

clear_log()

correcteur = "PID"

while 1:

    state = robot.state()
    old_distance_state = distance_state
    distance_state = state[0]
    angular_speed_state = state[3]
    old_angle = angle
    angle = math.pi / 180 * state[2] 

    angle = kalman.filter(angular_speed*math.pi/180, math.pi / 180 * state[2] )
    #angle = kalman.filter(angular_speed*math.pi/180, gyroscope.getAngle())

    reflection = colorController.sensor.reflection()
    if correcteur == "P":
        angular_speed = command.commandeP(reflection)

    elif correcteur == "PI":
        angular_speed = command.commandePI(reflection)

    elif correcteur == "PID":
        angular_speed = command.commandePID(reflection)

    elapsed_time = time.time() - timestamp
    timestamp = time.time()

    # First Method
    """
    x = x + speed * elapsed_time * math.cos((math.pi / 180 * angular_speed * elapsed_time + angle) / 2)
    y = y + speed * elapsed_time * math.sin((math.pi / 180 * angular_speed * elapsed_time + angle) / 2)

    #angle = angle + math.pi / 180 * angular_speed * elapsed_time
    write_log(x, y, angle, speed)
    """


    # Second Method

    x = x + (distance_state - old_distance_state) * math.cos((angle + old_angle) / 2)
    y = y + (distance_state - old_distance_state) * math.sin((angle + old_angle) / 2)

    write_log(x, y, angle, speed)


    # Third Method
    """
    x, y = gyroscope.getCoordinate()
    write_log(x, y, gyroscope.angle, speed)
    """

    robot.drive(speed, angular_speed)
