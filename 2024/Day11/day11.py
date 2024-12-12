# day09.py
# from numba import jit
from functools import cache

testcases = ['0 1 10 99 999', '125 17', '6563348 67 395 0 6 4425 89567 739318']
blink = {0: {"result": [1], "count": 0}} 

@cache
def check_and_add(stone: int) -> None:
    if stone not in blink.keys():
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

# @cache
# def recurse_stone_to_step(stone,step):
#     resulting_stones = blink[stone]["result"]
#     for rs in resulting_stones:
#         if step == 1:
#             blink[rs]["count"] += 1
#         else:
#             recurse_stone_to_step(rs,step-1)

@cache
def recurse_stone_to_step(stone,step) -> int:
    resulting_stones = blink[stone]["result"]
    if step == 1:
        return len(resulting_stones)
    else:
        return sum([recurse_stone_to_step(rs,step-1) for rs in resulting_stones])
        
        
def main():
    input = testcases[2]
    stones = list(map(int,input.split()))
    
    part_1 = part_2 = 0
    
    for stone in stones:
        check_and_add(stone)
    
    part_2 = 0
    for stone in stones:
        part_1 += recurse_stone_to_step(stone,25)
        part_2 += recurse_stone_to_step(stone,75)
        
    # part_2 = sum([blink[stone]["count"] for stone in blink.keys()])
            
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')



if __name__ == "__main__":
    main()