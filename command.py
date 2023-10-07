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

class Command:
    
    consigne = 50
    sumErreur = 0
    
    colorChanged = False
    previousErreur = 0
    previousColor = "Black"
    currentColor = "Black"

    def __init__(self, k, ki, kd, tau, sumBorn, speed):
        self.k = k
        self.ki = ki
        self.kd = kd
        self.tau = tau
        self.sumBorn = sumBorn
        self.speed = speed

    def computeSumError(self, erreur):
        self.sumErreur += erreur
        if abs(self.sumErreur) > self.sumBorn:
            if self.sumErreur < 0:
                self.sumErreur = -self.sumBorn
            else:
                self.sumErreur = self.sumBorn
    
    def commandeP(self, reflection):
        angle = 0
        erreur = abs(reflection-self.consigne)
        if reflection > 50:
            angle = self.k*erreur
        else:
            angle = -self.k*erreur
        #print(math.log(erreur))
        wait(self.tau * 500)
        return angle

    def commandePI(self, reflection):
        angle = 0
        erreur = abs(reflection-self.consigne)
        self.computeSumError(erreur)

        angle =  self.k*erreur + self.ki*self.tau*self.sumErreur

        if reflection > 50:
            self.currentColor = "White"
        else:
            angle =  -angle
            self.currentColor = "Black"

        if self.currentColor != self.previousColor:
            self.sumErreur = 0

        self.previousColor = self.currentColor
        wait(self.tau * 500)
        return angle


    def commandePID(self, reflection):
        angle = 0
        erreur = abs(reflection-self.consigne)
        self.computeSumError(erreur)

        angle =  self.k*erreur + self.ki*self.tau*self.sumErreur + (self.kd/self.tau)*(erreur - self.previousErreur)

        if reflection > 50:
            self.currentColor = "White"
        else:
            self.currentColor = "Black"
            angle = -angle

        if self.currentColor != self.previousColor:
            self.sumErreur = 0

        self.previousColor = self.currentColor
        self.previousErreur = erreur
        wait(self.tau * 500)
        return angle