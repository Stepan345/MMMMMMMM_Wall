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
open = {}
closed = {}
bounds = 12
#print(aren)
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
    neighbours={}
    for i in aroundCords:
        x = i[0]+active[0]
        y = i[1]+active[1]
        traversable = True
        for obj in gc.get_objects():
            if isinstance(obj, Obsticle) and listsMatch(aroundCords,obj.points()):
                traversable = False
                break
        if x < 0 or y<0 or x>bounds or y>bounds:
            traversable = False
        if str(x)+str(y) in closed or not traversable:
                continue
        gCost = math.floor(math.sqrt(pow((x)-car.pos[0],2)+pow((y)-car.pos[1],2))*10)
        hCost = math.floor(math.sqrt(pow((x)-dest[0],2)+pow((y)-dest[1],2))*10)
        fCost = hCost + gCost
        neighbours[str(x)+str(y)] = {
            'pos':[x,y],
            'name': str(x)+str(y),
            'fCost': fCost,
            'gCost': gCost,
            'hCost': hCost
        }
    return neighbours

def findPath(dest:list[int]):
    current = {
        'pos':[],
        'name': 0,
        'fCost':1000,
        'gCost':1000,
        'hCost':1000,
        'path':0,
        'parent': str(car.pos[0])+str(car.pos[1])
    }
    open[str(car.pos[0])+str(car.pos[1])] = {
        'pos':car.pos,
        'name':str(car.pos[0])+str(car.pos[1]),
        'fCost':0,
        'gCost':0,
        'hCost':0,
        'path': 0,
        'parent': str(car.pos[0])+str(car.pos[1])
    }
    while(True):
        if current['name'] in open:
            closed[current['name']] = open[current['name']]
            del open[current['name']]
        tempCount = 0
        for i in open.values():
            if(tempCount==0):
                current = i
            if i['fCost'] < current['fCost']:
                current = i
            elif i['fCost'] == current['fCost'] and i['hCost'] > current['hCost']:
                current = i
            tempCount+=1
        if(current['pos'][0] == dest[0] and current['pos'][1] == dest[1]):
            break
        #print(str(current)+'\n-------------------')
        nodes = checkNodes(current['pos'],dest)
        #print(str(nodes)+'\n-------------------')
        for i in nodes.values():
            if not i['name'] in open:
                open[i['name']] = {
                    'pos':i['pos'],
                    'name':i['name'],
                    'hCost':i['hCost'],
                    'gCost':i['gCost'],
                    'fCost':i['fCost'],
                    'path':current['path']+1,
                    'parent':current['name']
                }
            if open[i['name']]['path'] > current['path']+1:
                open[i['name']]['path'] = current['path']+1
                open[i['name']]['parent'] = current['name']
    print(str(current)+'\n-------------------')
    objectFollow = current['parent']
    finOut = [[current['parent'],current['fCost']]]
    for n in range(0,current['path']-1):
        objectFollow = closed[objectFollow]['parent']
        finOut.append([closed[objectFollow]['name'],closed[objectFollow]['fCost'],])
    return finOut




#cords start at 0
print(findPath([6,9]))
#findPath([5,9])

