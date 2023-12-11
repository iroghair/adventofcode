import re
import numpy as np
import time
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from itertools import repeat

def import_data(infile):
    with open(infile,'r') as file:
        raw = file.readlines()

    data = [line.rstrip() for line in raw]

    # Find start position
    start = 0
    data.insert(0,'.'*len(data[0]))
    data.append('.'*len(data[0]))
    for r,_ in enumerate(data):
        data[r] = '.'+data[r]+'.'
        try:
            start = r,data[r].index('S')
        except:
            continue
                
    return data,start

def idx(r,c): 
    return r*len(data[0]) + c if r>=0 and c>= 0 and r<=len(data) and c<= len(data[0]) else 0

def coo(idx): 
    return [idx//len(data[0]), idx%len(data[0])]

def get_connected_nb(r,c):
    sym = data[r][c]
    if sym == '|':
        nb = [idx(r-1,c),idx(r+1,c)]
    elif sym == '-':
        nb = [idx(r,c-1),idx(r,c+1)]
    elif sym == '7':
        nb = [idx(r,c-1),idx(r+1,c)]
    elif sym == 'J':
        nb = [idx(r-1,c),idx(r,c-1)]
    elif sym == 'F':
        nb = [idx(r,c+1),idx(r+1,c)]
    elif sym == 'L':
        nb = [idx(r,c+1),idx(r-1,c)]
    elif sym == 'S':
        nb = []
        if data[r][c+1] in 'J-7':
            nb.append(idx(r,c+1))
        if data[r][c-1] in 'FL-':
            nb.append(idx(r,c-1))
        if data[r+1][c] in '|JL':
            nb.append(idx(r+1,c))
        if data[r-1][c] in '|F7':
            nb.append(idx(r-1,c))
    else:
        nb = []

    return nb

def flatten(m):
    return [item for row in m for item in row]

def setup_graph(data,startpos):
    nnodes = len(data)*len(data[0])
    g = np.zeros((nnodes,nnodes))
    taxidist = np.zeros((len(data),len(data[0])))

    for r,line in enumerate(data):
        for c,sym in enumerate(line):
            if sym == '.':
                continue
            else:
                id = idx(r,c)
                id_to_nb = get_connected_nb(r,c)
                for nb in id_to_nb:
                    nb_to_id = get_connected_nb(*coo(nb))
                    if id in nb_to_id:
                        g[id][nb] = 1

    idx_start = idx(*startpos)

    # for i in range(taxidist.shape[0]), for j in range(taxidist.shape[1]):

    A = shortest_path(csgraph=g,directed=False,indices=idx_start)
    # print(A.reshape(len(data[0]),len(data)))
    print(np.max(A, where=~np.isinf(A),initial=0))
    exit()

def run_part_1(data):
    ans_pt1 = ...

    print(f'Part 1: {ans_pt1}')

def run_part_2(data):
    ans_pt2 = ...

    print(f'Part 2: {ans_pt2}')

if __name__ == '__main__':
    part2 = False
    infile = 'input.txt'
    data,startpos = import_data(infile)

    setup_graph(data,startpos)
    tstart = time.time_ns()
    run_part_1(data)
    print(f'Part 1 finished in {time.time_ns() - tstart} us')
    
    if part2:
        tstart = time.time()
        run_part_2(data)
        print(f'Part 2 finished in {time.time() - tstart} s')
        

   
                        