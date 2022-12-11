import numpy as np
import matplotlib.pyplot as plt


def write_positions(posH, posT):
    A = [ ['.' for _ in range(6)] for _ in range(6)]
    A = np.array(A)
    A[posT[0],posT[1]] = 'T'
    A[posH[0],posH[1]] = 'H' 

    print(np.flip(A,axis=1).T, '\n')

myfile = 'input.txt'

with open(myfile, 'r') as file:
    lines = file.readlines()

posH,posT = [np.array([0,0]) for _ in range(2)]
write_positions(posH, posT)

tail_locations = np.array([posT])

for line in lines:
    move = line.split()[0]
    steps = line.split()[1]
    # Select appropriate move
    if move == 'R': move = np.array([1,0])
    elif move == 'L': move = np.array([-1,0])
    elif move == 'U': move = np.array([0, 1])
    elif move == 'D': move = np.array([0,-1])
    else: 
        print('No such move defined\n\n')
        exit()        
    
    # Take step, and check if tail needs to follow
    for n_moves in range(int(steps)):
        posH_old = posH.copy()
        posH += move
        if np.linalg.norm(posH-posT) >= 1.5:
            posT = posH_old
        tail_locations = np.append(tail_locations,[posT],axis = 0)
        # write_positions(posH, posT)

print(len(tail_locations), len(np.unique(tail_locations,axis=0)))

plt.plot(tail_locations[:,0],tail_locations[:,1],marker='o')
plt.ylabel('some numbers')
plt.show()