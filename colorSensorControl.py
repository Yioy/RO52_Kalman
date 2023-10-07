#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys

class ColorSensorControl:
    def __init__(self, sensorPort):
        self.sensor = ColorSensor(sensorPort)

    def color(self):
        return self.sensor.color()
    def reflection(self):
        return self.sensor.reflection()