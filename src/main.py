# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ssark                                                        #
# 	Created:      3/5/2024, 3:25:33 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import numpy as n
import math

# Brain should be defined by default
brain=Brain()
LeftGoalR = []
RightGoalR = []
LeftCupR = []
RightCupR = []
LeftGoalB = []
RightGoalB = []
LeftCupB = []
RightCupB = []
MiddleBlock = []
brain.screen.print("Hello V5")
def spinDeg(degrees):
    gyro.resetRotation()
    while(gyro.rotation(deg)<degrees):
        LDrive.spin(forward,(gyro.rotation(deg)/degrees)*10,pct)
        RDrive.spin(reverse,(gyro.rotation(deg)/degrees)*10,pct)
class Circle:
    def __init__(self,pos,color) -> None:
        self.pos = pos
        self.col = color
        self.width = 0 #tbd
    def distanceTo(self,obj):
        pos1 = obj.pos
        pos2 = self.pos
        dist = math.sqrt(((pos1[0]-pos2[0])*(pos1[0]-pos2[0]))+((pos1[1]-pos2[1])*(pos1[1]-pos2[1])))
        return dist
class Square:
    def __init__(self,pos,side) -> None:
        self.pos = pos
        self.greatestSize = math.sqrt(side*2)
        self.smallestSize = side
class Ball:
    def __init__(self,pos) -> None:
        self.pos = pos
    def distanceTo(self,obj):
        pos1 = obj.pos
        pos2 = self.pos
        dist = math.sqrt(((pos1[0]-pos2[0])*(pos1[0]-pos2[0]))+((pos1[1]-pos2[1])*(pos1[1]-pos2[1])))
        return dist
class Car:
    def __init__(self,position,rotation) -> None:
        self.pos = position
        self.rot = rotation
        self.visionOffset = 0#tbd
    def areaCheck(self):
        spinDeg(1)
        frontCheck = distance.objectDistance(inch)
        if(self.rotation>=-45 & self.rotation<=45) | (self.rotation<=-135&self.rotation>=135):incrament = 0
        else:incrament = 1
        
        
        
        



