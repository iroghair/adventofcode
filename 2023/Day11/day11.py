import re
import numpy as np
import time
from itertools import combinations

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()

    gloc = np.empty((0,2),dtype=np.int32)
    for i,line in enumerate(data):
        for res in re.finditer(r'\#',line):
            gloc = np.append(gloc,[[i,res.start()]],axis=0)

    size = (len(data),len(data[0]))
    return gloc,size

def run_part_1_2(gloc,size,expansion_factor):
    for x in range(size[0])[::-1]:
        if x not in gloc[:,0]:
            gloc[gloc[:,0]>x,0]+=(expansion_factor-1)
    for x in range(size[1])[::-1]:
        if x not in gloc[:,1]:
            gloc[gloc[:,1]>x,1]+=(expansion_factor-1)

    ans_pt1 = 0
    for pair in combinations(range(gloc.shape[0]),2):
        dist = np.linalg.norm(gloc[pair[0]]-gloc[pair[1]],1)
        if debug:
            print('Pair: ',pair, ' has a distance: ', dist)
        ans_pt1 += dist

    print(f'Part {part}: {ans_pt1}')


if __name__ == '__main__':
    infile = 'input.txt'
    debug = False
    gloc,size = import_data(infile)

    tstart = time.time()
    part = 1
    run_part_1_2(gloc.copy(),size,2)
    print(f'Part 1 finished in {time.time() - tstart} s')
    tstart = time.time()
    part = 2
    run_part_1_2(gloc,size,1_000_000)
    print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        