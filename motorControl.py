#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys

class MotorControl:
    def __init__(self, leftMotor, rightMotor):
        self.leftMotor = Motor(leftMotor)
        self.rightMotor = Motor(rightMotor)

    def forward(self, speed):
        self.leftMotor.run(speed)
        self.rightMotor.run(speed)

    #Considérant le sens horaire pour l'angle (droite = positif, gauche = négatif)
    def rotate(self, angle, aSpeed):
        if angle > 0:
            self.leftMotor.run_angle(aSpeed,angle*4)
        else:
            self.rightMotor.run_angle(aSpeed,-angle*4)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()