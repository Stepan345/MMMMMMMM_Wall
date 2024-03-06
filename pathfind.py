import math
import gc
import numpy
class Car:
    def __init__(self,position:list[int],dimentions:list[float]) -> None:
        self.pos = position
        self.dim = dimentions
        pass
    
class Obsticle:
    def __init__(self,position:list[int],width:int) -> None:
        self.pos = position
        self.width = width
        pass
    def points(self) -> list[list[int]]:
        contactPoints = []
        for x in range(0,self.width+1):
            for y in range(0,self.width+1):
                contactPoints.append([x+self.pos[0],y+self.pos[1]])
        return contactPoints


box = Obsticle([3,3],4)
car = Car([4,2],[2,2])
arena = numpy.ones([8,8,4],numpy.int16)
#print(arena)
aroundCords:list[list[int]] = []
for w in range(-1,2):
    for h in range(-1,2):
        if [w,h] != [0,0]:
            aroundCords.append([w,h])
def listsMatch(list1:list[list[int]], list2:list[list[int]]) -> bool:
    for sublist1 in list1:
        for sublist2 in list2:
            if sublist1 == sublist2:
                return True
    return False
def checkNodes(active:list[int],dest:list[int]):
    suround = numpy.full([3,3,3],300,numpy.int16)
    for i in aroundCords:
        if arena[i[0]+active[0],i[1]+active[1],0] == -1:continue
        for obj in gc.get_objects():
            if isinstance(obj, Obsticle) and listsMatch(aroundCords,obj.points()):
                arena[i[0]+active[0],i[1]+active[1]] = [-1,-1,-1]
        gCost = math.floor(math.sqrt(pow((i[0]+active[0])-car.pos[0],2)+pow((i[1]+active[1])-car.pos[1],2))*10)
        hCost = math.floor(math.sqrt(pow((i[0]+active[0])-dest[0],2)+pow((i[1]+active[1])-dest[1],2))*10)
        fCost = hCost + gCost
        suround[i[0]+1,i[1]+1] = [fCost,gCost,hCost]
    return suround

def findPath(dest:list[int]):
    activeNode = car.pos
    #while(activeNode != dest):
    nodes = checkNodes(activeNode,dest)
    for y in range(0,3):
        for x in range(0,3):
            print(nodes[y,x])
            if nodes[y,x][0] == 300:
                arena[activeNode[0],activeNode[1]] = [arena[activeNode[0],activeNode[1],0],arena[activeNode[0],activeNode[1],1],arena[activeNode[0],activeNode[1],2],0] 
                continue
            arena[(y-1)+activeNode[0],(x-1)+activeNode[1]] = [nodes[y,x,0],nodes[y,x,1],nodes[y,x,2],arena[(y-1)+activeNode[0],(x-1)+activeNode[0],3]]
    print(arena)

            
#cords start at 0
findPath([4,3])
#findPath([5,9])

