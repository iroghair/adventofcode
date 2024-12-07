# day06.py
import re
import numpy as np
from itertools import cycle

moves = [np.array(step) for step in [(-1,0), (0,1), (1,0), (0,-1)]]

def set_walked(grid,pos,walked=None):
    """Set up a matrix os zeros in which the walked positions can be indicated. The starting position is already indicated as a 1."""
    walked = np.zeros_like(grid)
    walked[tuple(pos)]=1
    return walked
    
def do_guard_walk(grid, pos, walked):
    """Let the guard walk across the domain until he meets an obstacle (nonzero value). The guard starts walking in the positive x direction. Record the walked positions with a 1 in the 'walked' matrix, and increase the obstacles he walks into by 1 each time. The function exits once the guard walks off-grid (no infinite loop), returning the total number of walked positions as a first return value, and in case the guard is stuck in an infinite loop, it returns 1 as a second value."""
    new_pos = pos
    for move in cycle(moves):
        new_pos = pos + move if np.any(new_pos >= grid.shape) else pos
        while grid[tuple(new_pos)] == 0:
            pos = new_pos
            walked[tuple(pos)] = 1
            new_pos = pos + move
            if np.any(new_pos >= grid.shape) or np.any(new_pos < (0,0)):
                return np.sum(walked.flatten()), 0
        grid[tuple(new_pos)] += 1
        # print(grid)
        if np.max(grid) == 6:
            return np.sum(walked.flatten()), 1
    
def main(infile):
    # infile = 'test.txt'
    with open(infile, 'r') as f:
        data = f.readlines()

    # Find the initial position of the guard 
    pos = np.array([(row,line.find('^')) for row, line in enumerate(data) if line.find('^') != -1]).squeeze()
    start = pos.copy()
    
    # Transform the input data into a np array, where 0 is a vacant position and 1 represents an obstacle.
    grid = [(line.strip().replace('.', '0').replace('#','1').replace('^','0')) for line in data]
    grid = np.array([[int(c) for c in line] for line in grid],dtype=np.int16)
    
    # Create an empty walked matrix to record the visited positions
    walked = set_walked(grid,pos)
    
    # Run the initial guard walk
    part_1,_ = do_guard_walk(grid, pos,walked)
    
    # Place an obstacle at each vacant position (except the guard start position) and count the number of infinite loops.
    openx,openy = np.where(walked==1)
    part_2 = 0
    for x,y in zip(openx,openy):
        if np.all((x,y) == start):
            continue
        grid_cp = grid.copy()
        grid_cp[x,y] = 1
        steps,p2 = do_guard_walk(grid_cp,start,walked)
        if p2 == 1:
            part_2 += p2
            print(x,y)

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')

if __name__ == "__main__":
    main("input.txt")
