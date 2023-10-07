#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import sys
import time
import math

class Leader:
    timestamp = time.time()
    elapsed_time = 0
    speed = 150
    flagMove = True
    server = BluetoothMailboxServer()
    mbox = TextMailbox('greeting', server)

    def __init__(self, time):
        self.time = time

    def move(self):
        self.elapsed_time = time.time() - self.timestamp
        if self.elapsed_time>self.time:
            self.timestamp = time.time()
            self.flagMove = not self.flagMove
        return self.flagMove

    def WaitForConnection(self):        
        # The server must be started before the client!
        print('waiting for connection...')
        self.server.wait_for_connection()
        print('connected!')
        return True
    
    def sendData(self, message):
        self.mbox.send(message)