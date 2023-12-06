import numpy as np
from itertools import islice
import sys
import time

# If Python.__version__ < 3.12
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
                # print(f'{self.name}-> src: {src} is in range: {maps[0]} and becomes {src+maps[2]}')
                return src+maps[2]
        # print(f'{self.name}-> src: {src} maps to {src}')
        return src # Default
        
    def map_reversed(self,src):
        for maps in self.rangelist:
            if src in maps[1]:
                return src-maps[2]
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

    return seeds,mlist
 
def run_part_1(seeds,mlist):
    minloc = sys.maxsize
    for seed in seeds:
        x = seed
        for maps in mlist:
            x = maps.map(x)
        minloc = min(x,minloc)

    print(f'Part 1: {minloc}')

def run_part_2(seeds,mlist):
    seeds = [range(int(x[0]),int(x[0])+int(x[1])) for x in batched(seeds,2)]
    location = -1
    found = False
    while not found:
        x = (location := location + 1)
        if location%1000000==0:
            print(f'Testing location: {location}++')
        for maps in mlist[::-1]:
            x = maps.map_reversed(x)

        for seedsr in seeds:
            if (x in seedsr):
                found = True
                print(f'Part 2: {location}')


if __name__ == '__main__':
    infile = 'input.txt'
    seeds,mlist = import_data(infile)

    start_pt1 = time.time()
    run_part_1(seeds,mlist)
    print(f'Runtime: {(time.time() - start_pt1)*1.0e6} us')
    
    start_pt2 = time.time()
    run_part_2(seeds,mlist)
    print(f'Runtime: {time.time() - start_pt2} s')
        

   
                        