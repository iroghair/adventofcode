import numpy as np
import time
from itertools import cycle
from math import prod

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

def run_part_2(moveseq,network):
    steplist = []
    for pos in [x for x in network.keys() if x[-1] == 'A']:
        steps = 0
        for move in cycle(moveseq):
            if pos[-1] == 'Z':
                break
            else:
                steps += 1
                pos = network[pos][move]
        steplist.append(steps)
    print(f'Part 2: {np.lcm.reduce(steplist)}')

if __name__ == '__main__':
    part1 = True
    part2 = True
    infile = 'input.txt'
    data = import_data(infile)

    init = 'AAA'
    goal = 'ZZZ'
    if part1:
        tstart = time.time()
        run_part_1(*data)
        print(f'Part 1 finished in {time.time() - tstart} s')
    
    if part2:
        tstart = time.time()
        run_part_2(*data)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        