import re
import numpy as np
import time
from functools import cache

def import_data(infile):
    """Load the infile, return a list of lines"""
    with open(infile,'r') as file:
        data = file.read().splitlines()
    return data

def run_part_1_2(data):
    """For all lines, process the card and accumulate the score. Also get copies of cards."""
    ans_pt1 = 0
    ncopies = np.zeros(len(data),dtype=np.int32)

    for n,_ in enumerate(data):
        winning_numbers = process_card(data,n)
        l = len(winning_numbers)
        ans_pt1 += 2**(l-1) if l>0 else 0
        ncopies += get_copies(n)

    ans_pt2 = np.sum(ncopies)
    return ans_pt1, ans_pt2

# @cache
def get_copies(n):
    """Get copies of the next few cards, based on the amount of winning numbers. Recursively determine
    if these cards win additional copies. Accumulate all copies in an array and return the array."""
    ncopies = np.zeros(len(data),dtype=np.int32)
    ncopies[n] += 1
    copies = range(n+1,n+1+len(process_card(data,n)))
    for card in copies:
        ncopies += get_copies(card)

    return ncopies

def process_card(data,cardno):
    """Get the card and match numbers and return the winning numbers"""
    gamesep = data[cardno].split(':')
    card_numbers = gamesep[1].split('|')[0].split()
    match_numbers = gamesep[1].split('|')[1].split()
    winning_numbers = [x for x in card_numbers if x in match_numbers]
    return winning_numbers

if __name__ == '__main__':
    infile = 'input.txt'
    data = import_data(infile)
    start = time.time()
    print(run_part_1_2(data))
    print(f'Finished in {time.time() - start} s')
        

   
                        