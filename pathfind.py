import math
import gc
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

box = Obsticle([3,3],4)
car = Car([4,2],[2,2])
def findPath(dest:list[int]):
    m = (car.pos[1]-dest[1])/(car.pos[0]-dest[0])
    #print(m)
    for i in range(car.pos[0]*10,dest[0]*10):
        for obj in gc.get_objects():
            if isinstance(obj, Obsticle):
                if obj.pos[0]+obj.width>i>obj.pos[0]:
                    pass
findPath([5,9])

