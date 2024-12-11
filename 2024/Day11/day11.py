# day09.py
import numpy as np

testcases = ['0 1 10 99 999', '125 17', '6563348 67 395 0 6 4425 89567 739318']

def main():
    input = testcases[2]
    stones = list(map(int,input.split()))
    
    part_1 = part_2 = 0
    
    # The work
    # print(stones)
    for step in range(25):
        insert_dict = {}
        for i,stone in enumerate(stones):
            strnum = str(stone)
            if stone == 0:
                stones[i] = 1
            elif len(strnum)%2 == 0:
                stones[i] = int(strnum[:len(strnum)//2])
                insert_dict[i+1] = int(strnum[len(strnum)//2:])
            else:
                stones[i] *= 2024
        # Insert new stones
        for inum,(key,val) in enumerate(insert_dict.items()):
            stones.insert(key+inum,val)
        # print(stones) 
    part_1 = len(stones)
    
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == "__main__":
    main()