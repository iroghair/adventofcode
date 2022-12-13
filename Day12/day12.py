from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np
import re

def get_index(i,j,nx):
    return j + i*nx

def get_neighbors(c,nx):
    i,j = divmod(c,nx)
    neighbors = list()
    neighbors.append(get_index(i-1,j,nx))
    neighbors.append(get_index(i+1,j,nx))
    neighbors.append(get_index(i,j-1,nx))
    neighbors.append(get_index(i,j+1,nx))
    neighbors = [x for x in neighbors if x>=0]
    return neighbors

if __name__ == "__main__":
    myfile = 'test.txt'

    with open(myfile, 'r') as file:
        data = file.read().splitlines()

    nx = len(data[0])
    A = np.empty((0,nx), int)

    while (data):
        row = np.array([[ord(x) for x in re.findall(r'.',data[0])]])
        A = np.append(A,row,axis=0)
        data.pop(0)
    
    A = np.reshape(A,(1,-1)).flatten()
    # Get start/end positions
    pos_start = np.where(A==ord('S'))
    pos_end   = np.where(A==ord('E'))

    # Set base line and set E to max(A)+1
    A -= ord('a')-1
    A[pos_start] = 0
    A[pos_end] = np.max(A)+1
    
    graph = csr_matrix(np.zeros((np.size(A),np.size(A))))
    # Create graph
    for c in np.nditer(A):
        for nb in get_neighbors(c,nx):
            if abs(A[c]-A[nb]) <= 1:
                graph[c,nb] = 1
            if A[c] >= A[nb]:
                graph[c,nb] = 1


    dist_matrix, predecessors = dijkstra(csgraph=graph, directed=False, indices=1, return_predecessors=True)
    print(dist_matrix[pos_end])
    print(predecessors)

