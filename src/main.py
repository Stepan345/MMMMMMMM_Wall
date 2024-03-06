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
class Circle:
    def __init__(pos,relatives):
        self.pos = pos
        self.width = diameter
        #the relatives don't do anything rn, but the goal is to use them to speed up the computing process in the future
        #self.rel = relatives.push(MiddleBlock)
    def distanceTo(obj):
        pos1 = obj.pos
        pos2 = self.pos
        dist = math.sqrt(((pos1[0]-pos2[0])*(pos1[0]-pos2[0]))+((pos1[1]-pos2[1])*(pos1[1]-pos2[1])))
        return dist
class Square:
    def __init__(pos,side):
        self.pos = pos
        self.greatestSize = math.sqrt(side*2)
        self.smallestSize = side

LeftGoalR = Circle([x,y],[RightGoalR,LeftCupR])
RightGoalR = Circle([x,y],[LeftGoal,RightCupR])
RightCupR = Circle([x,y],[RightGoalR,RightCupB])
LeftCupR = Circle([x,y],[LeftGoalR,LeftCupB])



