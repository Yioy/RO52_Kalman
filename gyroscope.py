#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys
import time
import math

class Gyroscope:
    X = 0
    Y = 0
    prev_angle = 0
    angle = 0
    timestamp = time.time()
    elapsed_time = 0
    #speed = 0

    def __init__(self, sensorPort, speed):
        self.sensor = GyroSensor(sensorPort, Direction.CLOCKWISE)
        self.resetAngle(0)
        self.speed = speed

    def getAngulaireSpeed(self):
        return self.sensor.speed()

    def setAngle(self):
        self.angle = (math.pi*self.sensor.angle())/180

    def getAngle(self):
        return (math.pi*self.sensor.angle())/180

    def resetAngle(self, angle):
        self.sensor.reset_angle(angle)

    def getCoordinate(self):
        self.elapsed_time = time.time() - self.timestamp
        self.timestamp = time.time()
        self.setAngle()
        self.X = self.X+self.speed*self.elapsed_time*math.cos((self.angle+self.prev_angle)/2)
        self.Y = self.Y+self.speed*self.elapsed_time*math.sin((self.angle+self.prev_angle)/2)
        self.prev_angle = self.angle
        #print("timeD = ", self.elapsed_time)
        return self.X, self.Y