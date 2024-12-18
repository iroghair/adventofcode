# day12.py
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from strgrid import strgrid, loc # Imported from Day08, I should make it a package some day

DEBUG = True
steps = ( loc((1,0)) , loc((-1,0)) , loc((0,1)) , loc((0,-1)) )

def parse(infile):
    with open(infile, 'r') as f:
        return strgrid(f.readlines())

def create_plot(garden: strgrid,start_xy):
    """Fill operation on garden plots. Return dictionary with set(coords) of the current plot, composed of continuous plant perks, and the plant name (note: the code here names a plot a contiguous region of the same plants, and does not align fully with the AoC description)
    """
    current_plant = garden[start_xy]
    current_plot = [start_xy]
    perimeter = 0
    outer_corners = 0
    for xy in current_plot:
        steps_to_fence = [] # Record the steps that lead to fence
        for step in steps:
            new_xy = loc(xy)+step
            # Fill operation: add new coordinates to list if they are inside the domain and the same plant
            if garden.is_inside(new_xy) and new_xy not in current_plot:
                if garden[new_xy] == current_plant: # and visited[new_xy] == '0':
                    current_plot.append(new_xy)
            # Perimeter operation: if the projected block xy is outside of the domain or has another plant, we need a fence:
            if not garden.is_inside(new_xy) or garden[new_xy] != current_plant:
                perimeter += 1
                steps_to_fence.append(step)
        # The total number of corners in a plot are equal to the number of sides of the plot
        # We can find the convex corners by recording the steps from each block xy leading to a fence
        # If we find a fence with 4 steps, the plot is a single block xy and has 4 corner points
        # If we find a fence with 3 steps, we have 2 corner points
        # If we find a fence with 2 steps, there is 1 corner, unless the fences are parallel
        # Parallel fences we can compute through summing the steps; if this yields (0,0) (e.g. (+1,0) and (-1,0)) the fences are parallel on that block
        match len(steps_to_fence):
            case 0 | 1: # No corners on this block
                continue                
            case 2: # Parallel fences when the sum of both steps equals (0,0)
                if steps_to_fence[0] + steps_to_fence[1] == (0,0):
                    continue
                else:
                    outer_corners += 1
            case 3:
                    outer_corners += 2
            case 4:
                    outer_corners += 4
    # We only detect convex corners on the plot, so the total corners of the plot is 2n-4
    outer_corners = 2*outer_corners - 4
    
    current_plot = set(current_plot)
    
    plot = {'Plant': current_plant, 'Coords': current_plot, 'Area': len(current_plot), 'Perimeter': perimeter, 'Outer corners': outer_corners, 'Inner corners': 0}
    return plot
    
def is_island(plot,plots, garden) -> bool:
    # plots.remove(plot)
    # Get coords around plot
    coords = set([loc(xy) + step for xy in plot['Coords'] for step in steps]).difference(plot['Coords'])# if garden.is_inside(loc(xy)+step)])
    print(f'Coords around plot: {coords}')
    
    # Check if the plot is adjacent to the field edge, in that case not an island
    for xy in coords:
        if not garden.is_inside(xy):
            return False
    
    neighbor_plot = garden[xy]
    for xy in coords:
        if garden[xy] != neighbor_plot:
            return False
    
    # Once we get here, the plot is an island and xy is a coordinate in the neighboring, surrounding plot
    # In that case, assign the number of outer corners of the current plot as inner corners
    print(f'Plot {plot} is an island with neighbor: {neighbor_plot}')
    for nb in plots:
        if xy in nb['Coords']:
            nb['Inner corners'] += plot['Outer corners']
            print(f'Sides of plot {nb['Plant']}: {nb['Inner corners'] + nb['Outer corners']}')
    return True
    
def main():
    part_1 = part_2 = 0
    infile = 'input.txt'
    # infile = 'test5.txt'
    garden = parse(infile)
    print(garden)
   
    plots = []
    for loc in garden.get_locations():
        if loc not in [x for xs in [list(plot.get('Coords',[])) for plot in plots] for x in xs]:
            plots.append(create_plot(garden,loc))

    part_1 = sum([plot['Area']*plot['Perimeter'] for plot in plots])
    
    for plot in plots:
        is_island(plot, plots.copy(), garden)
        
    for plot in plots:
        # Get coordinates of plot
        c = np.array(list(plot['Coords']))
        mx,mn = np.max(c,axis=0), np.min(c,axis=0)
        dim =  mx-mn+1
        plot_matrix = np.zeros(dim)
        plot_matrix[c[:,0]-mn[0],c[:,1]-mn[1]] = 1
        shift = np.array([[1,-1,0],[-1,1,0],[0,0,0]])
        a = sp.signal.convolve2d(plot_matrix,shift)
        total_sides = np.abs(a).sum()
        cost_of_plot = total_sides * plot['Area']
        if DEBUG:
            print(f'Cost for {plot['Plant']}: {cost_of_plot}, {total_sides=}')
        part_2 += cost_of_plot
    
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')  # 869438 too low
                                # 873584
                                # 886726 too high

if __name__ == "__main__":
    main()