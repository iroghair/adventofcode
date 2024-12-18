# day12.py
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from strgrid import strgrid, loc # Imported from Day08, I should make it a package some day

DEBUG = False
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
        for step in steps:
            new_xy = loc(xy)+step
            # Fill operation: add new coordinates to list if they are inside the domain and the same plant
            if garden.is_inside(new_xy) and new_xy not in current_plot:
                if garden[new_xy] == current_plant: # and visited[new_xy] == '0':
                    current_plot.append(new_xy)
            # Perimeter operation: if the projected block xy is outside of the domain or has another plant, we need a fence:
            if not garden.is_inside(new_xy) or garden[new_xy] != current_plant:
                perimeter += 1
    
    current_plot = set(current_plot)
    
    plot = {'Plant': current_plant, 'Coords': current_plot, 'Area': len(current_plot), 'Perimeter': perimeter}
    return plot
    
def main():
    part_1 = part_2 = 0
    infile = 'input.txt'
    # infile = 'test5.txt'
    garden = parse(infile)
    if DEBUG:
        print(garden)
   
    plots = []
    for loc in garden.get_locations():
        if loc not in [x for xs in [list(plot.get('Coords',[])) for plot in plots] for x in xs]:
            plots.append(create_plot(garden,loc))

    part_1 = sum([plot['Area']*plot['Perimeter'] for plot in plots])
        
    # Part 2
    for plot in plots:
        # Get coordinates of plot
        c = np.array(list(plot['Coords']))
        
        # Create a matrix containing the plot as 1 and add 0's elsewhere 
        mx,mn = np.max(c,axis=0), np.min(c,axis=0)
        plot_matrix = np.zeros(mx-mn+1)
        plot_matrix[c[:,0]-mn[0],c[:,1]-mn[1]] = 1
        
        # The filter array computes diagonal gradients, representing corners
        grad_diag = np.array([[1,-1,0],[-1,1,0],[0,0,0]])
        corners = sp.signal.convolve2d(plot_matrix,grad_diag)
        
        # Total sides is equal to the sum of all corners
        total_sides = np.abs(corners).sum()
        cost_of_plot = total_sides * plot['Area']
        if DEBUG:
            print(f'Cost for {plot['Plant']}: {cost_of_plot}, {total_sides=}')
        part_2 += cost_of_plot
    
    print(f'Part 1: {part_1}')
    print(f'Part 2: {int(part_2)}')

if __name__ == "__main__":
    main()