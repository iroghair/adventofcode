import re
import numpy as np

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()
    return data

def run_part_1(data):
    ans_pt1 = 0
    for line in data:
        gamesep = line.split(':')
        cardno = gamesep[0].split()[1]
        card_numbers = gamesep[1].split('|')[0].split()
        match_numbers = gamesep[1].split('|')[1].split()
        winning_numbers = [x for x in card_numbers if x in match_numbers]
        l = len(winning_numbers)
        ans_pt1 += (score := 2**(l-1) if l>0 else 0)
        # print(winning_numbers, score)     
    return ans_pt1

    print(f'Part 1: {ans_pt1}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part1 = True
    infile = 'input.txt'
    data = import_data(infile)

    if part1:
        print(run_part_1(data))
    else:
        run_part_2(data)
        

   
                        