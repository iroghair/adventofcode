# day06.py
import numpy as np

def parse_pt1(infile: str):
    data = [line.strip().split() for line in open(infile, 'r')]
    operators = data[-1]
    # Transpose the list for processing later
    data_T = list(map(list,zip(*data[:-1])))

    return data_T,operators

def parse_pt2(infile: str):
    with open(infile, 'r') as f:
        data = [line.replace('\n','') for line in f.readlines()[:-1]]

    # Rotate the list and join characters to form numbers again
    data_T = list(zip(*data))[::-1]
    numbers = [] # List of numbers of a single problem
    all_problems = [] # Collect all problems 
    for digits in data_T[::-1]:
        num = ''.join(digits).strip()
        if num == '':
            all_problems.append(numbers)
            numbers = []
        else:
            numbers.append(num)
    all_problems.append(numbers)
    
    return all_problems

def main(infile: str,debug: bool = False):
    nums,ops = parse_pt1(infile)
    part_1 = sum([int(eval(f'{op}'.join(line))) for op,line in zip(ops,nums)])
    print(f'Part 1: {part_1}')

    nums = parse_pt2(infile)
    part_2 = sum([int(eval(f'{op}'.join(line))) for op,line in zip(ops,nums)])
    print(f'Part 1: {part_2}')

if __name__ == "__main__":
    infile = 'input.txt'
    # infile = 'test.txt'
    main(infile)