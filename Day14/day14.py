import numpy as np
import re

class Sand():
    def __init__(self,A,source):
        self.A = A
        self.pos = source.copy()
        self.is_free = True
        self.in_abyss = False

    def move(self):
        x,y = self.pos[0], self.pos[1]
        yl = y + 1
        # Falls into abyss, mark the spot
        if yl >= np.shape(A)[1]:
            self.A[x,y] = 63
            self.is_free = False
            self.in_abyss = True
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
        paths = file.read()

    regex = re.findall(r'[0-9]*,[0-9]*', paths)
    pos = np.array([n.split(',') for n in regex], dtype=np.uint16)

    xmax,ymax = np.max(pos[:,0])+1, np.max(pos[:,1])+1
    A = np.zeros( (xmax,ymax), dtype=np.uint16)

    paths = paths.splitlines()
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

    n_sand = 0
    while (True):
        sand = Sand(A,sand_source)
        n_sand += 1
        while (sand.is_free):
            sand.move()
            print(n_sand)
        
        if sand.in_abyss:
            break


    print(n_sand-1)
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