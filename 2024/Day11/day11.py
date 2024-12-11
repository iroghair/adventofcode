# day09.py
import numpy as np

testcases = ['0 1 10 99 999', '125 17', '6563348 67 395 0 6 4425 89567 739318']
blink = {0: {"result": [1], "count": 0}} 

def check_and_add(stone: int) -> None:
    if stone not in blink.keys():
        # blink[stone]["count"] += 1
        # pass
    # else:
        strnum = str(stone)
        if len(strnum)%2 == 0: # Split stone into left and right
            left = int(strnum[:len(strnum)//2])
            right = int(strnum[len(strnum)//2:])
            blink[stone] = {"result":  [left,right], "count": 0}
            check_and_add(left)
            check_and_add(right)
        else:
            blink[stone] = {"result": [stone * 2024], "count": 0}
            check_and_add(stone * 2024)
    return

def recurse_stone_to_step(stone,step):
    resulting_stones = blink[stone]["result"]
    for rs in resulting_stones:
        if step == 1:
            blink[rs]["count"] += 1
        else:
            recurse_stone_to_step(rs,step-1)
        
        
def main():
    input = testcases[2]
    stones = list(map(int,input.split()))
    
    part_1 = part_2 = 0
    
    # The work for part 1 (left for historical reasons)
    print(stones)
    # for step in range(25):
    #     insert_dict = {}
    #     for i,stone in enumerate(stones):
    #         strnum = str(stone)
    #         if stone == 0:
    #             stones[i] = 1
    #         elif len(strnum)%2 == 0:
    #             stones[i] = int(strnum[:len(strnum)//2])
    #             insert_dict[i+1] = int(strnum[len(strnum)//2:])
    #         else:
    #             stones[i] *= 2024
    #     # Insert new stones
    #     for inum,(key,val) in enumerate(insert_dict.items()):
    #         stones.insert(key+inum,val)
    #     # print(stones) 
    # part_1 = len(stones)
    
    for stone in stones:
        check_and_add(stone)
        
    for stone in stones:
        recurse_stone_to_step(stone,75)
        
    part_2 = sum([blink[stone]["count"] for stone in blink.keys()])
            
    print(blink)
    
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')



if __name__ == "__main__":
    main()