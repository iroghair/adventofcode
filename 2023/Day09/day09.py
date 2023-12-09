import numpy as np
import time

def import_data(infile):
    data = list()
    for s in map(str.splitlines,open(infile)):
        data.append(np.array([int(x) for x in s[0].split()]))
    return data

def extrapolate(entry):
    a = b = 0
    differences = np.diff(entry)
    if not np.all(differences==0):
        a,b = extrapolate(differences)
    
    return entry[0]-a,b+entry[-1]
        
def run_part_1_2(data):
    ans = np.array([0,0])
    for entry in data:
        ans += extrapolate(entry)
    print(f'Part 1: {ans[1]}')
    print(f'Part 2: {ans[0]}')

if __name__ == '__main__':
    part2 = True
    infile = 'input.txt'
    data = import_data(infile)

    tstart = time.time()
    run_part_1_2(data)
    print(f'Part 1+2 finished in {time.time() - tstart} s')
    

   
                        