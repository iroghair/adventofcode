import re
import numpy as np

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()
    return data

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
        

   
                        