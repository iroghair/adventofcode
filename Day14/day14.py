import numpy as np
import re

class Sand():
    def __init__(self,A,source):
        self.A = A
        self.pos = source.copy()
        self.is_free = True

    def move(self):
        x,y = self.pos[0], self.pos[1]
        yl = y + 1
        # Falls into abyss, mark the spot
        if yl >= np.shape(A)[1]:
            self.A[x,y] = 63
            self.is_free = False
            return
        # Fall down, left or right
        if A[x,yl] == 0:
            self.pos += np.array([0,1])
        elif A[x-1,yl] == 0:
            self.pos += np.array([-1,1])
        elif A[x+1,yl] == 0:
            self.pos += np.array([1,1])
        else:
            # Stuck
            self.is_free = False
            self.A[x,y] = 128

if __name__ == '__main__':
    myfile = 'input.txt'
    sand_source = [500,0]

    with open(myfile,'r') as file:
        paths = file.read().splitlines()

    A = np.zeros((504,11),dtype=np.uint16)

    arr = np.empty((0,2), dtype=np.int16)
    for path in paths:
        segments = path.split(' -> ')
        for i in range(len(segments[:-1])):
            (xl,yl) = tuple([int(s) for s in segments[i].split(',')])
            (xh,yh) = tuple([int(s) for s in segments[i+1].split(',')])
            (xl,xh) = np.sort((xl,xh))
            (yl,yh) = np.sort((yl,yh))

            if (xl==xh):
                A[xl,yl:yh+1] = 255
            elif (yl==yh):
                A[xl:xh+1,yl] = 255
            else:
                print('Funny coordinate detected: ', segments[i] , ' -> ', segments[i+1])
                exit()

    # # Find abyss
    # walls_yx = np.where(A==255)
    # floor = np.max(walls_xy[1])
    # abyss = (np.min(np.where(A[floor,:]==255))-1, np.max(np.where(A[floor,:]==255))+1)
    # abyss_left = (floor,abyss[1])
    # abyss_right = (floor,abyss[0])

    n_sand = 0
    while (np.max(A[:,10])<=0):
        sand = Sand(A,sand_source)
        n_sand += 1
        while (sand.is_free):
            sand.move()
            print(n_sand)


    print(n_sand)
        # print('hoi')
        # A[1,10] = 1
# print(A)

if (False):
    xmin,xmax = (np.min(arr[:,0]),np.max(arr[:,0]))
    ymin,ymax = (np.min(arr[:,1]),np.max(arr[:,1]))
    print(xmin,xmax,ymin,ymax)
    A = np.zeros(( (xmax-xmin),(ymax-ymin)))
    print(A)

    for path in paths:
        arr = np.empty((0,2), dtype=np.int16)
        for coord_segment in path.split('->'):
            arr = np.append(arr,[np.array(re.findall(r'[0-9]+',coord_segment),dtype=np.int16)],axis=0)
        
        A = set_solid(A, arr,[xmin,ymin])
        A[arr]