import numpy as np
from scipy.signal import convolve2d

def main(fname: str, debug=False):
    # Import grid
    grid = np.array([list(map(int,line.strip().replace('.','0').replace('@','1'))) for line in open(fname, 'r')])
    # Convolution window
    mask = np.ones((3,3)); mask[1,1]=0
    
    it = 0
    total_accessible = 0
    ## Part 1
    while True:
        surrounding_rolls = convolve2d(grid,mask)
        accessible_rolls = np.where(surrounding_rolls[1:-1,1:-1]<4,1,0)*grid
        current_accessible = np.sum(accessible_rolls)
        if debug:
            print(f"Iteration: {it}\n",grid)
        
        if it == 0:
            print(f'Part 1: {current_accessible}')

        if current_accessible == 0:
            print(f'Part 2: {total_accessible}')
            break
        else:
            total_accessible += current_accessible
            grid -= accessible_rolls
            it += 1

if __name__ == "__main__":
    fname = 'test.txt'
    fname = 'input.txt'
    main(fname)