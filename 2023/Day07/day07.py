import re
import numpy as np
import time

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()

    hands = [x.split()[0] for x in data]
    bids = [int(x.split()[1]) for x in data]

    return hands, bids

def get_hand_type(hand):
    cards_in_hand = {card:0 for card in cards}
    # Get number of identical cards
    for card in hand:
        cards_in_hand[card] += 1
    
    same_max = max(cards_in_hand.values())

    if same_max == 5:
        return 'five'
    elif same_max == 4:
        return 'four'
    elif same_max == 1:
        return 'high'
    elif same_max == 3:
        if sorted(cards_in_hand.values())[-2] == 2:
            return 'full'
        else:
            return 'three'
    elif same_max == 2:
        if sorted(cards_in_hand.values())[-2] == 2:
            return 'two'
        else:
            return 'one'
    else:
        print('Edge case')
        exit()

def sort_key(hand):
    p = 0
    for i,single_card in enumerate(hand[::-1]):
        p += 13**i * cards.index(single_card)

    return p

def run_part_1(hands,bids):
    types = []
    for hand in hands:
        types.append(get_hand_type(hand))
        print(f'{hand} --> {types[-1]}')

    # Collect each type of hand in a list, together with the bids
    t_types = ["five","four","full","three","two","one","high"]
    hands_by_type = {t_type:[(hand,bid) for type,hand,bid in zip(types,hands,bids) if type == t_type] for t_type in t_types}
    
    # Sort each type list by the key
    for t_type in t_types:
        hands_by_type[t_type].sort(key=lambda c: sort_key(c[0]),reverse=True)

    c = 0
    score = 0
    for t_type in t_types[::-1]:
        for hand,bid in hands_by_type[t_type]:
            print(c,bid)
            score += (c := c + 1) * bid
    ans_pt1 = score

    print(f'Part 1: {ans_pt1}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part2 = False
    infile = 'input.txt'
    cards = 'AKQJT98765432'
    data = import_data(infile)

    tstart = time.time_ns()
    run_part_1(*data)
    print(f'Part 1 finished in {time.time_ns() - tstart} us')
    
    if part2:
        tstart = time.time()
        run_part_2(data)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        