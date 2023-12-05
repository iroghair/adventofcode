import re
import numpy as np
from itertools import islice
import sys

def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

class mapper:
    def __init__(self,name,ranges):
        self.name = name
        self.rangelist = []
        for r in batched(ranges,3):
            # Append a tuple that contains the source range, destination range and offset
            r = [int(x) for x in r]
            source = range(r[1],r[1]+r[2])
            dest = range(r[0],r[0]+r[2])
            offset = r[0]-r[1]
            self.rangelist.append((source,dest,offset))

    def map(self,src):
        for maps in self.rangelist:
            if src in maps[0]:
                print(f'{self.name}-> src: {src} is in range: {maps[0]} and becomes {src+maps[2]}')
                return src+maps[2]
        print(f'{self.name}-> src: {src} maps to {src}')
        return src # Default
        
def import_data(infile):
    with open(infile,'r') as file:
        data = file.read()

    seeds = data.splitlines()[0].split(':')[1].split()
    seeds = [int(x) for x in seeds]
    print(seeds)

    mlist = []
    for mapdata in data.split('\n\n')[1:]:
        data_in_set = mapdata.split()
        mlist.append(mapper(data_in_set[0],data_in_set[2:]))

    minloc = sys.maxsize
    for seed in seeds:
        x = seed
        for maps in mlist:
            x = maps.map(x)
        minloc = min(x,minloc)

    print(f'Part 1: {minloc}')
 
def run_part_1(data):
    ans_pt1 = ...

    print(f'Part 1: {ans_pt1}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part1 = True
    infile = 'test.txt'
    data = import_data(infile)

    if part1:
        run_part_1(data)
    else:
        run_part_2(data)
        

   
                        