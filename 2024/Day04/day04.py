# day04.py
import re
import numpy as np

def find_xmas(i,j,data):
    MtoS = {'M': 'S', 'S': 'M'}
    found = 0
    steps = [(x,y) for x in (-1,1) for y in (-1,1)]
    
    if i > 0 and i < len(data)-1 and j > 0 and j < len(data[i])-1:
        for step in steps:
            if data[i+step[0]][j+step[1]] == MtoS.get(data[i-step[0]][j-step[1]], 'q') and data[i-step[0]][j+step[1]] == MtoS.get(data[i+step[0]][j-step[1]], 'q2'):
                found += 1
                break
    return found

def find_mas(i,j,data):
    found = 0
    steps = [(x,y) for x in (-1,0,1) for y in (-1,0,1)]
    for step in steps:
        if i + step[0]*3 < 0 or i + step[0]*3 >= len(data) or j + step[1]*3 < 0 or j + step[1]*3 >= len(data[i]):
            continue
        next_x, next_y = i,j
        to_find = 'MAS'
        while to_find != '':
            next_x,next_y = next_x + step[0], next_y + step[1]
            if data[next_x][next_y] == to_find[0]:
                to_find = to_find[1:]
            else:
                break
        if to_find == '':
            found += 1
    return found
        
def main(infile):
    # infile = 'test.txt'
    D = {'X': 1, 'M': 2, 'A': 3, 'S': 4}
    s_input = []
        
    with open(infile, 'r') as f:
        data = f.readlines()
    
    part_1 = part_2 = 0
    for i,line in enumerate(data):
        for j,c in enumerate(line.strip()):
            if c == 'X':
                part_1 += find_mas(i,j,data)
            if c == 'A':
                part_2 +=  find_xmas(i,j,data)
        
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')

if __name__ == "__main__":
    main("input.txt")
