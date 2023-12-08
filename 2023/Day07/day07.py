import re
import numpy as np
import time

def import_data(infile):
    """Import the data file and split between two columns: first column contains 
    the hands (str), second column contains the bids (int). Returned as separate lists"""
    with open(infile,'r') as file:
        data = file.read().splitlines()

    hands = [x.split()[0] for x in data]
    bids = [int(x.split()[1]) for x in data]

    return hands, bids

def get_hand_type(hand,part=1):
    """Get the scoring type of a given hand, returns a str containing:
    five: five of a kind
    four: four of a kind
    full: full house
    three: three of a kind
    two: two pairs
    one: one pair
    high: high card

    When part=2, any J (Joker) on hand will be added to the highest non-J card count.
    """
    cards_in_hand = {card:0 for card in cards}
    # Get number of identical cards
    for card in hand:
        cards_in_hand[card] += 1
    
    if part==2:
        n_jokers = cards_in_hand["J"]
        sorted_by_amount = sorted(cards_in_hand.items(),key=lambda c: c[1])
        highest_card_count_not_J = sorted_by_amount[-1] if sorted_by_amount[-1][0] != 'J' else sorted_by_amount[-2]
        cards_in_hand[highest_card_count_not_J[0]] += n_jokers
        cards_in_hand["J"] = 0

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
    """Provide a sorting key based on the card hierarchy and their relative positions. 
    Low sort key means highest value."""
    p = 0
    for i,single_card in enumerate(hand[::-1]):
        p += 13**i * cards.index(single_card)

    if debug:
        print(hand,p)

    return p

def run_part_1_2(hands,bids,part=1):
    """Evaluate the type of hand (e.g. three of a kind, two pair, ...), and sort all hands of the same type into lists. Then sort by score in each type list. Finally, make an account of the total earnings (position * bid)"""
    types = []
    for hand in hands:
        types.append(get_hand_type(hand,part))
        if debug:
            print(f'{hand} --> {types[-1]}')

    # Collect each type of hand in a list, together with the bids
    hands_by_type = {t_type:[(hand,bid) for type,hand,bid in zip(types,hands,bids) if type == t_type] for t_type in score_types}
    
    # Sort each type list by the key
    for t_type in score_types:
        hands_by_type[t_type].sort(key=lambda c: sort_key(c[0]),reverse=True)

    c = 0
    score = 0
    for t_type in score_types[::-1]:
        for hand,bid in hands_by_type[t_type]:
            score += (c := c + 1) * bid
            if debug:
                print(c,bid)
    ans_pt1 = score

    print(f'Part {part}: {ans_pt1}')

if __name__ == '__main__':
    part2 = True
    debug = False
    
    # Common
    infile = 'input.txt'
    score_types = ["five","four","full","three","two","one","high"]
    data = import_data(infile)
    
    # Part 1
    cards = 'AKQJT98765432'
    tstart = time.time()
    run_part_1_2(*data)
    print(f'Part 1 finished in {time.time() - tstart} s')
    
    if part2:
        cards = 'AKQT98765432J'
        tstart = time.time()
        run_part_1_2(*data,2)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        