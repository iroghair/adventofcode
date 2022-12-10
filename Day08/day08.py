import numpy as np
from scipy.sparse import csr_matrix

myfile = 'test.txt'

with open(myfile, 'r') as file:
    data = file.read().splitlines()

mat = np.array([[int(x) for x in str(line)] for line in data])
# print(mat)
N,M = np.shape(mat)

# maxrows = np.amax(mat,axis=1)
# maxcols = np.amax(mat,axis=0)
A = np.zeros(np.shape(mat))
A[:,0] = A[:,-1] = A[0,:] = A[-1,:] = 1

# max_row_idx = np.argmax(mat,axis=1)
# max_col_idx = np.argmax(mat,axis=0)
# print('Max in rows: ',maxrows,     'Max in cols: ', maxcols)
# print('Max row idx: ',max_row_idx, 'Max col idx: ', max_col_idx)

# Part 1
for i in range(np.shape(mat)[0]):
    # Look over columns
    trees,idx = np.unique(np.maximum.accumulate(mat[:,i]),return_index=True)
    A[idx,i] = 1
    trees,idx = np.unique(np.maximum.accumulate(np.flip(mat[:,i])),return_index=True)
    A[N-idx-1,i] = 1
    trees,idx = np.unique(np.maximum.accumulate(mat[i,:]),return_index=True)
    A[i,idx] = 1
    trees,idx = np.unique(np.maximum.accumulate(np.flip(mat[i,:])),return_index=True)
    A[i,M-idx-1] = 1

print(A,int(np.sum(A)))

exit()

    
    # # Rows from left
    # row = np.array([1,2,3,6,5,4,6,7])
    # # Find tree sizes from a view point
    
    
    
    # trees, idx = np.unique(row, return_index=True)
    # a = np.array(row[int(idx)])
    # the_diff = np.diff(idx)
    # # Get an array with the unique trees at their relative positions
    # print('Row: ', row, 'Unique trees: ', trees, 'Index:', idx, 'Diff: ', np.diff(idx))

    # np.extract(the_diff)
    # for i in range(len(the_diff)):
    #     np.array(rows)
    #     s = np.empty((0,0))
    # # the_diff = np.append(True,np.diff(idx)>0)
    # # # Use row(idx) if diff(idx)>0
    # # for x,i in enumerate(idx):
    # #     if (the_diff[i]>0):
    # #         print(row[idx[x]])

    # cut_trees = np.zeros(len(trees))
    # [row(x) for x in idx]
    # np.put(cut_trees, idx, trees) 
    # # print(row, trees, idx)

    # while (len(row)):
    #     print(i)


    # a  = mat[i][0:np.argmax(mat[i])+1]
    # print('i = ',i, 'a = ', a)
    # # Rows from qright
    # a  = mat[i][-1:np.argmax(mat[i][::-1])-1:-1]
    # print('i = ',i, 'a = ', a)