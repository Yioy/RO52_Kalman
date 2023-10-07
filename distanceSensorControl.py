
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys

class DistanceSensorControl:
    def __init__(self, sensorPort):
        self.sensor = UltrasonicSensor(sensorPort)
    
    def getDistance(self):
        return self.sensor.distance()

    def getPresence(self, distance):
        print(self.getDistance())
        return (self.getDistance() < distance)
