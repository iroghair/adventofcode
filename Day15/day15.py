import re
import numpy as np

def get_within_MH_dist_coords(dist, source, line, track, offset):
    base = np.array([(i,dist-i) for i in range(dist+1)])
    base = np.append(base, base*[-1,1],axis=0)
    base = np.append(base, base*[1,-1],axis=0)
    base = np.append(base, base*[-1,-1],axis=0)
    base = np.unique(base,axis=0)
    base += source - offset
    idx = np.where(base[:,1]==line-offset[1])
    if np.shape(idx)[1] > 1:
        from_to = np.sort([base[idx][0,0],base[idx][1,0]])
        track[from_to[0]:from_to[1]+1] = 1
        # print(track)
    return track

def get_MH_dist_coords(dist):
    base = np.array([(i,dist-i) for i in range(dist+1)])
    base = np.append(base, base*[-1,1],axis=0)
    base = np.append(base, base*[1,-1],axis=0)
    base = np.append(base, base*[-1,-1],axis=0)
    return np.unique(base,axis=0)

myfile = 'input.txt'
with open(myfile, 'r') as file:
    data = file.readlines()

# Get all the number data
num = np.array([re.findall(r'[0-9]+',line) for line in data],dtype=np.int64)

# Overkill, but it does the trick (also compute neg offset)
xmax = np.max(np.array([num[:,0]+num[:,2]]))
ymax = np.max(np.array([num[:,1]+num[:,3]]))
xmin = np.min(np.array([num[:,0]-num[:,2]]))
ymin = np.min(np.array([num[:,1]-num[:,3]]))
print('Max size of domain: ',xmax-xmin,ymax-ymin)

# A = np.zeros( (xmax-xmin,ymax-xmin), dtype=np.int64)
track = np.zeros((xmax-xmin,))
offset = np.array([xmin,ymin])
line = 10
for n,i in enumerate{num}:
    # Central coordinate
    c = (n[0],n[1])
    # Get MH distance of nearest beacon
    dist = abs(n[2]-n[0]) + abs(n[3]-n[1])
    # Get indices from central node
    print(f'Processing line {i} with coordinates {n}\n')
    track = get_within_MH_dist_coords(dist, c, line, track, offset)

for n in num:
    # Coordinate of beacon
    beacon = (n[2],n[3])
    if beacon[1] == line:
        track[n[2]-offset[0]] = 0

print(f'Number of locations on line {line} where beacon cannot exist: {np.shape(np.where(track>0))[1]}')

# for n in num:
#     # Central coordinate (correct for negative offset)
#     c = (n[0]+xmin, n[1]+ymin)
#     # Get MH distance of nearest beacon
#     dist = abs(n[2]-n[0]) + abs(n[3]-n[1])
#     # Get indices from central node
#     base = get_MH_dist_coords(dist)
#     for ix in c[0]+base[:,0]:
#         for iy in c[1] + base[:,1]:
#             print(ix,iy)
#             A[ix,iy] = -1

#     print(A)

    # A[, c[1]+base[1,:]] = 1
    # A[]
