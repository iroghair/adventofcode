# day13.py
import numpy as np
from itertools import batched
import re

DEBUG = False

def cramers(A,b):
    """Solve Ax=b and return solution for a 2x2 system, return (0,0) if singular."""
    D = A[0,0]*A[1,1]-A[0,1]*A[1,0]
    return (0,0) if D == 0 else (b[0]*A[1,1] - b[1]*A[0,1])/D, (b[1]*A[0,0]-b[0]*A[1,0])/D


def main():
    solution = np.zeros(2)
    infile = 'input.txt'
    # infile = 'test.txt'

    with open(infile, 'r') as f:
        for block in batched(f.readlines(),4):
            data = '\n'.join([line.strip() for line in block if line != '\n'])
            A = np.array(re.findall(r'(?<=[X|Y]\+)\d*',data,re.M),dtype=np.int64).reshape(2,2).T
            b = np.array(re.findall(r'(?<=[X|Y]\=)\d*',data,re.M),dtype=np.int64)
            for i,added_pos in enumerate([0,10_000_000_000_000]):
                tokens = cramers(A,b+added_pos)
                cost = 3*tokens[0] + tokens[1] if all([int(n)==n for n in tokens]) else 0
                if DEBUG:
                    print(f'For solution {i+1}: {tokens=}, {cost=}')
                    print(f'System of eqns: {A=}\n{b=}')
                solution[i] += cost

    print(f'Part 1: {int(solution[0])}') 
    print(f'Part 2: {int(solution[1])}') 

if __name__ == "__main__":
    main()    