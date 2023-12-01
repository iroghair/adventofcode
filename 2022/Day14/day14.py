import numpy as np
import matplotlib.pyplot as plt
import re
import time


class Sand():
    def __init__(self,A,source):
        self.A = A
        self.pos = source.copy()
        self.is_free = True
        self.in_abyss = False

    def move(self):
        x,y = self.pos[0], self.pos[1]
        yl = y + 1
        # Falls into abyss, mark the spot (part 2: creates the floor)
        if yl >= np.shape(self.A)[1]:
            self.A[x,y] = 63
            self.is_free = False
            self.in_abyss = True
            return
        # Fall down, left or right
        if self.A[x,yl] == 0:
            self.pos += np.array([0,1])
        elif self.A[x-1,yl] == 0:
            self.pos += np.array([-1,1])
        elif self.A[x+1,yl] == 0:
            self.pos += np.array([1,1])
        else:
            # Stuck: deposit sand particle
            self.is_free = False
            self.A[x,y] = 128

def set_up_solid_fragments(paths,A):
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

def get_matrix(paths):
    regex = re.findall(r'[0-9]*,[0-9]*', paths)
    pos = np.array([n.split(',') for n in regex], dtype=np.uint16)
    xmax,ymax = np.max(pos[:,0])+1, np.max(pos[:,1])+1
    return np.zeros( (xmax,ymax), dtype=np.uint16)

if __name__ == '__main__':
    myfile = 'input.txt'
    sand_source = [500,0]

    with open(myfile,'r') as file:
        paths = file.read()

    # Preallocate matrix using max(x,y) in the input 
    A = get_matrix(paths)

    # Set up the solid fragments in the matrix
    set_up_solid_fragments(paths,A)

    # Part 1
    plt.ion()
    fig1, (ax1, ax2) = plt.subplots(2,1)
    n_sand = 0
    sand = Sand(None,sand_source)
    while (not sand.in_abyss):
        sand = Sand(A,sand_source)
        n_sand += 1
        while (sand.is_free):
            sand.move()

        # axim1.set_data(A.T)
        # fig1.canvas.flush_events()

    print('Part 1: Number of sand particles deposited before one lands in the abyss: ',n_sand-1)
    axim1 = ax1.imshow(A.T,cmap='jet_r',interpolation='none')

    plt.show()

    # Part 2
    A2 = np.zeros((np.shape(A)[0]*2,np.shape(A)[1]+2))
    set_up_solid_fragments(paths,A2)
    n_sand = 0
    while int(A2[sand_source[0],sand_source[1]]) == 0:
        sand = Sand(A2,sand_source)
        n_sand += 1
        while (sand.is_free):
            sand.move()

    print('Part 2: Number of sand particles to reach the top: ', np.shape(np.where(A2==128))[1]) 

    axim2 = ax2.imshow(A2.T,cmap='jet_r',interpolation='none')
    plt.show(block=True)