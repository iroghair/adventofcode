# day02.py
import numpy as np
import itertools as it

def check_row(row):
    dA = np.diff(row)
    within_increment_limits = np.all(np.abs(dA) <= 3)
    monotonous_series = np.abs(np.sum(np.sign(dA))) == dA.shape
    return within_increment_limits and monotonous_series

def read_file(infile):
    with open(infile,'r') as file:
        return file.read().splitlines()

if __name__ == "__main__":
    infile = 'input.txt'
    data = read_file(infile)
    p1 = p2 = 0
    for line in data:
        row = np.array(list(map(int,line.split())))
        if check_row(row):
            p1 += 1
        else:
            # Remove elements to see if the row works
            for n in range(len(row)):
                if check_row(np.delete(row,n)):
                    p2 += 1
                    break

    print(f'Part 1: {p1}')
    print(f'Part 2: {p2+p1}')
