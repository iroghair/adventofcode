import numpy as np
from scipy.sparse import csr_matrix

myfile = 'input.txt'

with open(myfile, 'r') as file:
    data = file.read().splitlines()

mat = np.array([[int(x) for x in str(line)] for line in data])
# print(mat)
N,M = np.shape(mat)

# maxrows = np.amax(mat,axis=1)
# maxcols = np.amax(mat,axis=0)
A = np.zeros(np.shape(mat))
B = np.ones(np.shape(mat))
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

print('Total trees visible: ', int(np.sum(A)))

for i in range(1,N-1):
    for j in range(1,M-1):
        # Look right:
        nbtrees = mat[i,j+1::]
        factor = 0
        # score_right = sum(range <= mat[i,j])
        for k in range(nbtrees.size):
            factor += 1
            if nbtrees[k] >= mat[i,j]:
                break
        score_right = factor
        
        # Look left:
        nbtrees = mat[i,0:j:][::-1]
        factor = 0
        for k in range(nbtrees.size):
            factor += 1
            if nbtrees[k] >= mat[i,j]:
                break
        score_left = factor

        # Look up:
        nbtrees = mat[0:i:,j][::-1]
        factor = 0
        for k in range(nbtrees.size):
            factor += 1
            if nbtrees[k] >= mat[i,j]:
                break
        score_up = factor

        # Look down:
        nbtrees = mat[i+1::,j]
        factor = 0
        for k in range(nbtrees.size):
            factor += 1
            if nbtrees[k] >= mat[i,j]:
                break
        score_down = factor

        B[i,j] = score_down * score_up * score_left * score_right

        # # score_right = max(1,sum(mat[i,j+1::] < mat[i,j]))
        # score_right = sum(np.maximum.accumulate(mat[i,j+1::]) < mat[i,j])
        # B[i,j] *= score_right
        # print('score right: ', score_right)
        # # Look left:
        # # score_left = max(1,sum(mat[i,j-1:1:] < mat[i,j]))
        # score_left = sum(mat[i,0:j:][::-1] < mat[i,j])
        # B[i,j] *= score_left
        # print('score left: ', score_left)
        # # Look up:
        # score_up = max(1,sum((np.maximum.accumulate(mat[0:i:,j][::-1])) < mat[i,j]))
        # #max(1,sum(mat[i-1:1:,j] < mat[i,j]))
        # B[i,j] *= score_up
        # print('score up: ',score_up)
        # # Look down:
        # # score_down = max(1,sum(mat[i+1::,j] < mat[i,j]))
        # score_down = max(1,sum((np.maximum.accumulate(mat[i+1::,j])) < mat[i,j]))
        # B[i,j] *= score_down
        # print('score down: ', score_down)
        # # print(i,j,a)

print('Total score per tree: \n', B)
print('Maximum score: ', np.max(np.max(B)))

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