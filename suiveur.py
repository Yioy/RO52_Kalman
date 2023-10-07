#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from distanceSensorControl import DistanceSensorControl
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
import sys
import time
import math

class Suiveur:
    distanceController = DistanceSensorControl(Port.S2)
    previousDistance = distanceController.getDistance()
    speedCoeff = 0
    speedSlowDown = 0
    speedAccel = 0
    previousCoef = 0

    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev-2'
    client = BluetoothMailboxClient()
    mbox = TextMailbox('greeting', client)

    def __init__(self, a, d, af, df, ac, dc):
        self.a = a
        self.d = d
        self.af = af
        self.df = df
        self.ac = ac
        self.dc = dc

    def move(self):
        if self.distanceController.getPresence(150):
            return False
        else:
            return True

    def move1Point(self):
        self.speedCoeff = max(min(50, self.a*(self.previousDistance-self.d)), 0) / 100
        self.previousDistance = self.distanceController.getDistance()
        return self.speedCoeff

    def move2Point(self):
        self.speedSlowDown = min(max(0, self.af*(self.previousDistance-self.df)), 50)
        self.speedAccel = min(max(self.ac*(self.previousDistance-self.dc), 0, self.speedCoeff),50)
        self.speedCoeff = min(self.speedAccel, self.speedSlowDown) / 100
        print(self.speedCoeff)
        self.previousDistance = self.distanceController.getDistance()
        return self.speedCoeff
    
    def connect(self):
        print('establishing connection...')
        self.client.connect(self.SERVER)
        print('connected!')
        return True
    
    def receiveData(self):
        # In this program, the client sends the first message and then waits for the
        # server to reply.
        # self.mbox.send('hello!')
        # self.mbox.wait()
        #print(self.mbox.read())
        return self.mbox.read()



