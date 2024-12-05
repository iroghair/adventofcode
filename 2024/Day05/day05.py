# day04.py
import re
import numpy as np
from itertools import combinations

def create_index(orders):
    idx = dict()
    for order in orders:
        if order[0] in idx.keys():
            idx[order[0]].append(order[1])
        else:
            idx[order[0]] = [order[1]]
    return idx

def get_center_page_p1(manual,idx):
    for (p1,p2) in combinations(manual,2):
        if p1 in idx.get(p2,[]):
            return 0
    return manual[len(manual)//2]

def get_center_page_p2(manual,idx,has_changed=False):
    for  (p1,p2) in combinations(manual,2):
        if p1 in idx.get(p2,[]):
            i,ii = manual.index(p1),manual.index(p2)
            manual[i], manual[ii] =  manual[ii], manual[i]
            return get_center_page_p2(manual, idx, True)
    return manual[len(manual)//2] if has_changed else 0
    
def main(infile):
    # infile = 'test.txt'
    part_1 = 0
    with open(infile, 'r') as f:
        page_orders = [tuple(item) for item in [map(int,line.strip().split('|')) for line in f.readlines() if line.find('|') != -1]]
        f.seek(0)
        manuals = [list(item) for item in [map(int,line.strip().split(',')) for line in f.readlines() if line.find(',') != -1]]
    idx = create_index(page_orders)
    
    part_1 = sum([get_center_page_p1(manual,idx) for manual in manuals])
    part_2 = sum([get_center_page_p2(manual,idx) for manual in manuals])

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')

if __name__ == "__main__":
    main("input.txt")
