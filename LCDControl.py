#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys

class LCDControl:
    def __init__ (self, color, distance):
        self.display = brick.display()


    def status():
        display.clear()
        display.text("Color : ")
        display.text("Distance : ")