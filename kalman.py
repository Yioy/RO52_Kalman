#!/usr/bin/env pybricks-micropython
import sys
import time
import math

class Kalman:
    angle = 0
    angleV = 0.1
    def __init__(self, processN, kPID, V0, angle0, O):
        self.processN = processN
        self.kPID = kPID
        self.VEstPrevious = V0
        self.angleEstPrevious = angle0
        self.O = O
    
    def filter(self, angleN, angleGyro):

        self.VEstPrevious = self.VEstPrevious + self.O
        K = self.VEstPrevious/(self.VEstPrevious+self.processN)
        self.angleEstPrevious = self.angleEstPrevious + self.kPID*angleN + self.processN
        Y = angleGyro - self.angleEstPrevious
        self.angleEstPrevious = self.angleEstPrevious + K*Y
        self.VEstPrevious = (1-K)*self.VEstPrevious
        return self.angleEstPrevious