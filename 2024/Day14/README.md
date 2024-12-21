# README.md Day 14

We need to find the position of the robots after $N$ time steps. 

## Part 1
Using `numpy` this is not very difficult: we can simply add $N=100$ times the velocity to the position array, and use `np.mod` to wrap around in the given size of the 2D domain. The total cost is the product of the number of robots in each quadrant (excluding the centerlines).

```{python}
def compute_part_1(pos,vel):
    """Compute the position after 100 steps, and use module to wrap the boundaries around. Count all robots in each quadrant and return the product of these numbers."""
    pos = np.mod(pos + 100*vel,SIZE)
    ...
```

This uses an expansion of the 2D domain (i.e. a 2D matrix in which each element represents the number of robots at that position):

```{python}
def expand_domain(pos):
    """Create a 2D array containing the number of robots at each position."""
    domain = np.zeros(shape=SIZE,dtype=int)
    for p in pos:
        domain[tuple(p)] += 1
    return domain
```

The iterative part is not very elegant, but it's fast nonetheless. I will look for a vectorized way of accumulating the robots. 

## Part 2

I already made a function to visualise the positions of the robots:

```{python} 
def show_pattern(pos,vel,tim):
    """Using the original pos and vel, plot the positions of the robots at time=tim."""
    ...
```

At first I looked at the first 200 images, then resorted to making a movie of 100,000 images but could not find the right image. I analysed the maximum number of robots at a single position for each time step, but this did not work either. Finally, I realised that a Christmas tree would likely have the robots aligned mostly diagonally, so I use a convolution mask shaped X, and use the time step that has a maximum of this procedure:

```{python}
def compute_part_2(pos,vel):
    """Use a diagonal convolution mask to check on which time step we find robots diagonally aligned. Compute the maximum of the convoluted array to find a degree of 'diagonalism' in the current time step. Plot this max vs time, and return the absolute transient maximum."""
    
    # Create identity matrix + add its mirror to find X-patterns
    match = np.eye(15)
    match += match[::-1]
    maxima = []
    # The robot positions are recurrent every 10,000 steps or so
    for t in range(1,10_000):
        pos = np.mod(pos + vel,SIZE)
        result = sp.signal.convolve2d(expand_domain(pos),match)
        out = result.max()
        maxima.append(out)

    return np.argmax(maxima)+1
```

This yields the right time step. In hindsight, I could have looked also for robots aligned horizontally or vertically.