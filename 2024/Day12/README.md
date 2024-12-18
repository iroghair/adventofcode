# README.md Day 12
We need to obtain the area and perimeter of garden plots. These are used to compute the final cost, being the answer.

## Part 1
The first task is to compute the total perimeter and area. I perform a fill operation starting at (0,0), looking at all direct neighbors and comparing the plant type (same type means same plot) to find a contiguous plot area. While the coordinate list fills up (and it may contain duplicates that are removed later by a set operation), I check around each newly added block to detect whether they are adjacent to either the total garden edge (array bounds) or adjacent to a different plant type. In these cases, I add 1 to the perimeter.

```{python}
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
                if garden[new_xy] == current_plant:
                    current_plot.append(new_xy)
            # Perimeter operation: if the projected block xy is outside of the domain or has another plant, we need a fence:
            if not garden.is_inside(new_xy) or garden[new_xy] != current_plant:
                perimeter += 1
                steps_to_fence.append(step)

    current_plot = set(current_plot)
    
    plot = {'Plant': current_plant, 'Coords': current_plot, 'Area': len(current_plot), 'Perimeter': perimeter}
    return plot
```

I store the results in a dictionary, and the computation of the cost per plot and overall is trivial.

### Considerations

* I was using a 'visited' array first, but this is not needed if we check whether a coordinate is already inside the current coordinate list
* Another improvement may be to not create a list of coordinates, but a set immediately. #TODO

## Part 2

The total number of fences (regardless of the length) is equal to the number of corners of the shape. 

### Attempt 1
At first, I tried to count which steps (+1,0), (0,-1) etc lead to a differnt plant or edge, which would define the number of convex corners:

* If we find a fence with 4 steps, the plot is a single block xy and has 4 corner points
* If we find a fence with 3 steps, we have 2 corner points
* If we find a fence with 2 steps, there is 1 corner, unless the fences are parallel
    * Parallel fences we can compute through summing the steps; if this yields (0,0) (e.g. (+1,0) and (-1,0)) the fences are parallel on that block

```{python}
# We can find the convex corners by recording the steps from each block xy leading to a fence
for xy in current_plot:
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
```

Afterwards, we can account for the undetected concave corners of the shape by

```{python}
outer_corners = 2*outer_corners - 4
```

But, for edge cases like below it does not work.

```
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
```

I also tried to detect island plots (a plot isolated inside a single other plot), using:

```{python}
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
```

This works, and does a good job in obtaining the (so far) undetected concave corners. But, a lot of additional logic would be needed to use these island plots (and islands in islands) for the right number of corners. This is not the way.

### Attempt 2
I considered using a Laplacian operator, or an interpolation of (-0.5,-0.5) so that we are using the grid intersections (nodes) instead of the cell values. I read up on the Harris-Laplace operator and tested first and second order derivatives, as well as interpolations, but this cannot be done elegantly for such few limited cases.

### Attempt 3
Taking the idea of using a Laplacian (convolution) mask on each plot (where the plot is extracted into a separate array, marked 1 and all blocks that do not belong to it are marked 0), and I changed the mask to represent the four diagonals from a given node. This yields a matrix with the absolute values representing the number of corners for a given cell (the mask is shifted towards the lower (x,y) direction but in principle any shift would work). The total number of corners is simply the sum of the absolute values in that matrix.

The implementation can then also be done more elegantly:
```{python}
    for plot in plots:
        # Get coordinates of plot
        c = np.array(list(plot['Coords']))
        # dim =  mx-mn+1
        
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
```
