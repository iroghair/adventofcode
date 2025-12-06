# day06.py
import numpy as np

def parse(infile: str):
    data = [line.strip().split() for line in open(infile, 'r')]
    operators = data[-1]
    # Transpose the list for processing later
    data_T = list(map(list,zip(*data[:-1])))

    numbers = [[int(num) for num in line] for line in data[:-1]]

    return data_T,operators

def main(infile: str,debug: bool = False):
    part_1 = part_2 = 0
    nums,ops = parse(infile)

    part_1 = sum([int(eval(f'{op}'.join(line))) for op,line in zip(ops,nums)])

    print(f'Part 1: {part_1}')




if __name__ == "__main__":
    infile = 'input.txt'
    # infile = 'test.txt'
    main(infile)