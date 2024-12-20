# day14.py
import matplotlib as mpl
import numpy as np
import re
from itertools import batched
import matplotlib.pyplot as plt

SIZE = (101,103)
# SIZE = (11,7) # Test

def parse(infile):
    with open(infile, 'r') as f:
        pos_vel = re.findall(r'-?\d*,-?\d*',f.read(),re.M)
    pos = np.array([[int(d) for d in pv[0].split(',')] for pv in batched(pos_vel,2)])[::-1]
    vel = np.array([[int(d) for d in pv[1].split(',')] for pv in batched(pos_vel,2)])[::-1]
    return pos,vel

def main():
    part_1 = part_2 = 0
    infile = 'input.txt'
    # infile = 'test.txt'
    pos,vel = parse(infile)
    # pos = pos[1,:]
    # vel = vel[1,:]

    demo = np.zeros(shape=SIZE,dtype=int)
    for p in pos:
        demo[tuple(p)] += 1
    print(demo.T)
    pos = np.mod(pos + 100*vel,SIZE)
    demo.fill(0)
    for p in pos:
        demo[tuple(p)] += 1
    print(demo.T)
    
    center = (np.array(SIZE)+1)//2
    print(center)

    A = [demo[:center[0]-1,:center[1]-1].sum(),
         demo[center[0]:,:center[1]-1].sum(),
         demo[:center[0]-1,center[1]:].sum(),
         demo[center[0]:,center[1]:].sum()]
    print(A)
    part_1 = np.prod([a.sum() for a in A])

    print(f'Part 1: {part_1}')

if __name__ == "__main__":
    main()