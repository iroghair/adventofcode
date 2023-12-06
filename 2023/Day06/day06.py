import re
import numpy as np
from scipy.optimize import fsolve
from math import floor

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()

    time = [int(x) for x in data[0].split(':')[1].split()]
    dist = [int(x) for x in data[1].split(':')[1].split()]

    return time,dist

def run_part_1_2(trace,drace):
    total_nways_pt1 = 1
    for b,c in zip(trace,drace):
        # Get the roots of the parabolic equation, make sure that it is strictly above by subtracting eps
        roots = np.roots([-1,b,-c-1e-13])
        # Floor the number since we can only use discrete ms units
        roots = [floor(x) if floor(x)!=x else floor(x-1) for x in roots]
        nways = abs(roots[0] - roots[1])
        total_nways_pt1 *= nways

    print(f'Part 1: {total_nways_pt1}')

    # Sigh... Putting it all back together
    b = int(''.join([str(t) for t in trace]))
    c = int(''.join([str(d) for d in drace]))
    roots = np.roots([-1,b,-c-1e-13])
    roots = [floor(x) if floor(x)!=x else floor(x-1) for x in roots]
    nways_pt2 = abs(roots[0] - roots[1])
    print(f'Part 2: {nways_pt2}')
    return total_nways_pt1, nways_pt2

if __name__ == '__main__':
    part1 = True
    infile = 'input.txt'
    time,dist = import_data(infile)

    run_part_1_2(time,dist)
        

   
                        