# day14.py
import matplotlib.pyplot as plt
import numpy as np
import re
from itertools import batched
import time
import scipy as sp


SIZE = (101,103)
DEBUG = False
# SIZE = (11,7) # Test

def parse(infile):
    """Read the input file into 2 2xN arrays: pos and vel"""
    with open(infile, 'r') as f:
        pos_vel = re.findall(r'-?\d*,-?\d*',f.read(),re.M)
    pos = np.array([[int(d) for d in pv[0].split(',')] for pv in batched(pos_vel,2)])[::-1]
    vel = np.array([[int(d) for d in pv[1].split(',')] for pv in batched(pos_vel,2)])[::-1]
    return pos,vel

def expand_domain(pos):
    """Create a 2D array containing the number of robots at each position."""
    domain = np.zeros(shape=SIZE,dtype=int)
    for p in pos:
        domain[tuple(p)] += 1
    return domain

def show_pattern(pos,vel,tim):
    """Using the original pos and vel, plot the positions of the robots at time=tim."""

    # Compute position
    pos = np.mod(pos + tim*vel,SIZE)
    domain = expand_domain(pos)
    
    # Plot
    fig, ax = plt.subplots()
    mat = ax.matshow(domain.T, cmap='viridis')
    mat.set_clim(vmin=0, vmax=4)
    fig.tight_layout()
    plt.colorbar(mat, ax=ax)
    plt.show()   
    
def compute_part_1(pos,vel):
    """Compute the position after 100 steps, and use module to wrap the boundaries around. Count all robots in each quadrant and return the product of these numbers."""
    pos = np.mod(pos + 100*vel,SIZE)
    domain = expand_domain(pos)
    if DEBUG:
        print(domain)
    
    center = (np.array(SIZE)+1)//2
    if DEBUG:
        print(center)

    A = [domain[:center[0]-1,:center[1]-1].sum(),
         domain[center[0]:,:center[1]-1].sum(),
         domain[:center[0]-1,center[1]:].sum(),
         domain[center[0]:,center[1]:].sum()]
    return np.prod([a.sum() for a in A])

def compute_part_2(pos,vel):
    """Use a diagonal convolution mask to check on which time step we find robots diagonally aligned. Compute the maximum of the convoluted array to find a degree of 'diagonalism' in the current time step. Plot this max vs time, and return the absolute transient maximum."""
    
    # Create identity matrix + add its mirror to find X-patterns
    match = np.eye(15)
    match += match[::-1]
    maxima = []
    # The robot positions are recurrent every 10,000 steps or so
    for t in range(1,10_000):
        if DEBUG and t%1000 == 0:
            print(f'{t=}')
        pos = np.mod(pos + vel,SIZE)
        domain = expand_domain(pos)
        result = sp.signal.convolve2d(domain,match)
        out = result.max()
        maxima.append(out)
        
    plt.plot(range(1,t+1),maxima, 'x')
    plt.show()
    return np.argmax(maxima)+1

def main():
    part_1 = part_2 = 0
    infile = 'input.txt'
    # infile = 'test.txt'
    pos,vel = parse(infile)

    max_diags = compute_part_2(pos,vel)
    show_pattern(pos,vel,max_diags)
    print(f'Part 1: {compute_part_1(pos,vel)}')
    print(f'Part 2: {max_diags}')
    
if __name__ == "__main__":
    main()