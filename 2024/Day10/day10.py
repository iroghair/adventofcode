# day09.py
import numpy as np
from itertools import pairwise

steps = ( (+1,0) , (-1,0) , (0,+1) , (0,-1) )
end_points = set()
DEBUG = False

def parse(infile: str) -> np.ndarray:
    """Open the file and return a numpy array (2D) with the data"""
    with open(infile, 'r') as f:
        return np.array([[int(i) if  i!='.' else -1 for i in line.strip() ] for line in f.readlines()])

def is_inside(data: np.ndarray,loc: np.ndarray) -> bool:
    """Check whether a location lies within the grid boundaries"""
    return all([0<=l<data.shape[i] for i,l in enumerate(loc)])
    
def take_steps(data: np.ndarray,loc: np.ndarray) -> int:
    """Starting at loc, attempt to take all possible steps <,>,^,v in the data. Check whether the 
       move is valid, and if so, check whether the height step is +1 with respect to the previous
       position. If we reach the summit, add the end-point as a valid end point to a global list,
       (for part 1) and increment the number of valid trails by 1 (for part 2).
       
       TODO: It might be nice to store also the trail breadcrumbs and plot it
       """
    score = 0
    height = data[tuple(loc)]
    for step in steps:
        if is_inside(data, new_loc := loc + step):
            new_height = data[tuple(new_loc)]
            if new_height == height + 1:
                if DEBUG:
                    print(f'{loc} -> {new_loc}')
                if new_height == 9:
                    if DEBUG:
                        print(f'Finished this trail')
                    end_points.add(tuple(new_loc))
                    score += 1
                else:
                    score += take_steps(data,new_loc)
    return score

def main():
    infile = 'input.txt'
    part_1 = part_2 = 0
    
    data = parse(infile)
    print(data)
    
    # Loop over all trailheads and search for good trails leading to the summit
    for sx,sy in zip(*np.where(data == 0)):
        end_points.clear()
        total_trails = take_steps(data, np.array([sx,sy]))
        score = len(end_points)
        if DEBUG:
            print(f'Trailhead at {(sx,sy)} has {score = } and {total_trails = }')
        part_1 += score
        part_2 += total_trails
    
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == "__main__":
    main()