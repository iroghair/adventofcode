import re
import numpy as np
from scipy.spatial.distance import pdist 
from collections import deque

def get_range_per_row(dist, source, ranges):
    """Get all distance nodes _at_ MH distance"""

    # Just the plain MH distance into positive (x,y) space from source
    base = [(source[0]-i,i+source[0],source[1]-(dist-i),dist-i+source[1]) for i in range(dist+1)]
    for b in base:
        if b[2] >= 0 and b[2] < 4000000:
            ranges[b[2]].append([b[0],b[1]])
        if b[3] >= 0 and b[3] < 4000000:
            ranges[b[3]].append([b[0],b[1]])

    return ranges

myfile = 'input.txt'
maxdomain = 4000000
with open(myfile, 'r') as file:
    data = file.readlines()

# Get all the number data
num = np.array([re.findall(r'-?[0-9]+',line) for line in data],dtype=np.int64)

# Overkill, but it does the trick (also compute neg offset)
xmax = np.max(np.array([num[:,0]+num[:,2]]))
ymax = np.max(np.array([num[:,1]+num[:,3]]))
xmin = np.min(np.array([num[:,0]-num[:,2]]))
ymin = np.min(np.array([num[:,1]-num[:,3]]))
print('Max size of domain: ', xmax-xmin, ymax-ymin)

suspects = np.array([[0,0]])
no_beacon = np.array([[0,0]])
offset = np.array([xmin,ymin])
ranges = []
for _ in range(maxdomain):
    ranges.append(deque())

for n in num:
    # Central coordinate
    c = (n[0],n[1])
    # Get MH distance of nearest beacon
    dist = abs(n[2]-n[0]) + abs(n[3]-n[1])
    # Get indices from central node
    print(f'Processing line with coordinates {n}')
    ranges = get_range_per_row(dist, c, ranges)

print('Starting line-by-line analysis...')
n=maxdomain-1
current_range = [0,maxdomain]
while current_range[0] <=0 and current_range[1] >= maxdomain:
    sorted_range = sorted(ranges[n])
    current_range = sorted_range[0]
    for r in sorted_range:
        if r[0] <= current_range[1] and r[1] > current_range[1]:
            current_range[1] = r[1]
    n -= 1


print(n, current_range)
print(f'Beacon is at position {current_range[1]+1}, {n+1}, answer is {4000000*(current_range[1]+1) + (n+1)}')

# First answer: (2889605,3398894) (top-down) (forgot correcting n 🙄)
# second answer: (2889605,3398892) (bottom-up) (forgot it again, but the lower y value gave it away)
# Correct answer: (2889605,3398893) (bottom-up, corrected n) -->