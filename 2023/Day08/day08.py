import re
import numpy as np
import time
from itertools import cycle

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()

    moveseq = [int(move) for move in data[0].replace('L','0').replace('R','1')]
    network = {line[:3]:(line[7:10],line[12:15]) for line in data[2:]}
    return moveseq,network

def run_part_1(moveseq,network):
    pos = init
    steps = 0
    for move in cycle(moveseq):
        if pos == goal:
            break
        else:
            steps += 1
            pos = network[pos][move]

    print(f'Part 1: {steps}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part2 = False
    infile = 'input.txt'
    data = import_data(infile)

    init = 'AAA'
    goal = 'ZZZ'
    tstart = time.time_ns()
    run_part_1(*data)
    print(f'Part 1 finished in {time.time_ns() - tstart} us')
    
    if part2:
        tstart = time.time()
        run_part_2(data)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        