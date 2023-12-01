from scipy.sparse import lil_matrix
from scipy.sparse.csgraph import dijkstra
import  matplotlib.pyplot as plt
import numpy as np
import re

def get_index(i,j,nx):
    return j + i*nx

def get_neighbors(c,nx,ny):
    i,j = divmod(c,nx)
    neighbors = list()
    neighbors.append(get_index(i-1,j,nx))
    neighbors.append(get_index(i+1,j,nx))
    neighbors.append(get_index(i,j-1,nx))
    neighbors.append(get_index(i,j+1,nx))
    neighbors = [x for x in neighbors if x>=0 and x<nx*ny]
    return neighbors

if __name__ == "__main__":
    myfile = 'input.txt'

    with open(myfile, 'r') as file:
        data = file.read().splitlines()

    nx = len(data[0])
    ny = len(data)
    A = np.empty((0,nx), int)

    while (data):
        row = np.array([[ord(x) for x in re.findall(r'.',data[0])]])
        A = np.append(A,row,axis=0)
        data.pop(0)
    
    B = A.copy()

    A = np.reshape(A,(1,-1)).flatten()
    # Get start/end positions
    pos_start = np.where(A==ord('S'))
    pos_end   = np.where(A==ord('E'))

    # Set base line and set E to max(A)+1
    A -= ord('a')-1
    A[pos_start] = 0
    A[pos_end] = np.max(A)+1
    
    graph = lil_matrix(np.zeros((np.size(A),np.size(A))))
    # Create graph
    for c in range(np.size(A)):
        for nb in get_neighbors(c,nx,ny):
            if abs(A[c]-A[nb]) <= 1:
                graph[c,nb] = graph[nb,c] = 1
            if A[c] >= A[nb]:
                graph[c,nb] = 1


    # Part 1
    dist_matrix, predecessors = dijkstra(csgraph=graph, directed=True, return_predecessors=True,indices=pos_start)
    print('Part 1: Distance from position S: ', dist_matrix.flatten()[pos_end])
    
    # Get shortest path by backtracking:
    path_nodes = list()
    node = predecessors.flatten()[pos_end]
    while (node != pos_start):
        path_nodes.append(int(node))
        node = predecessors.flatten()[node]

    path_nodes.append(int(pos_start[0]))
    path_xy = np.array([divmod(c,nx) for c in path_nodes])

    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.imshow(B,cmap='gist_earth')
    ax1.plot(np.array(path_xy)[:,1],np.array(path_xy)[:,0])

    # ax2 = plt.subplot(212,projection='3d')
    # xgrid,ygrid = np.meshgrid(range(0,nx), range(0,ny))
    # surf = ax2.plot_surface(xgrid, ygrid, np.reshape(A,(ny,nx)), cmap='coolwarm',
    #                    linewidth=0, antialiased=False)
    # ax2.set_box_aspect(aspect = (2,1,1))
    # ax2.plot(np.array(path_xy)[:,1],np.array(path_xy)[:,0],A[path_nodes])

    plt.show()
    # Part 2
    dist_matrix = dijkstra(csgraph=graph, directed=True, indices=np.where(A==1),min_only=True)
    print('Part 2: Distance from any position a: ', dist_matrix.flatten()[pos_end])
    
