import re
import numpy as np
import time

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().split('\n\n')
    
    return data

def find_mirror(mat):
    for i in range(1,mat.shape[0]):
        

def run_part_1(data):
    for line in data:
        line = line.replace('#','1').replace('.','0')
        sz = [len(line.replace('\n','')),line.index('\n')]
        sz[0] //= sz[1]
        print(sz)
        p = np.fromstring(line.replace('\n',''), dtype='b', sep='')-48
        p = p.reshape(sz[0],sz[1])
        print(p)

    ans_pt1 = ...

    print(f'Part 1: {ans_pt1}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part2 = False
    infile = 'test2.txt'
    data = import_data(infile)

    tstart = time.time_ns()
    run_part_1(data)
    print(f'Part 1 finished in {time.time_ns() - tstart} us')
    
    if part2:
        tstart = time.time()
        run_part_2(data)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        