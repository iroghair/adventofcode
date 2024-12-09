# day07.py
from itertools import pairwise
from math import prod
import numpy as np
import random


def parse(infile):
    with open(infile, 'r') as f:
        return {int(line.split(':')[0]):list(map(int,line.split()[1:])) for line in f.readlines()}

def concat(values):
    return int(''.join([str(v) for v in values]))
    
def compute(outcome: int, values: list, concat:bool):
    s = sum(values[0:2])
    p = prod(values[0:2])
    c = concat(values[0:2]) if concat else 0
    if len(values) <= 2:
        return outcome in [s,p,c]

    return compute(outcome, [s] + values[2:]) or compute(outcome, [p] + values[2:]) or (compute(outcome, [c] + values[2:]) and concat)
        
def main():
    infile = 'test.txt'
    infile = 'input.txt'
    data = parse(infile)
    
    part_1 = part_2 = 0
    for key,val in data.items():
        if compute(key,val):
            print(f'{key=}, {val=}')
            part_1 += key

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}') # 13189134363890 too low
                               # 106016739583593 too high
                               # 106016739583593
                               # 106016735664498

if __name__ == "__main__":
    main()
