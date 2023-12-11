import numpy as np
import time

def import_data(infile):
    data = list()
    for s in map(str.splitlines,open(infile)):
        data.append(np.array([int(x) for x in s[0].split()]))
    return data

def get_poly_coeffs(entry):
    out = 0
    differences = np.diff(entry)
    if not np.all(differences==0):
        out = get_poly_coeffs(differences)+1

    return out

def get_fit(entry,deg):
    p = np.polyfit(np.arange(len(entry)),entry,deg,full=True)
    if p[1].shape != (0,):
        print(entry)
        p = np.polyfit(np.arange(len(entry)),entry,deg,full=True)
    return p[0]

def run_part_1_2(data):
    np.seterr(all='warn')
    ans = np.array([0,0])
    for entry in data:
        deg = get_poly_coeffs(entry)+1
        print('Fit a polynomial with degree ',deg)
        p = get_fit(entry,deg)
        ans[0] += np.round(np.polyval(p,len(entry)))
        ans[1] += np.round(np.polyval(p,-1))
    print(f'Part 1: {ans[0]}')
    print(f'Part 2: {ans[1]}')

if __name__ == '__main__':
    part2 = True
    infile = 'input.txt'
    data = import_data(infile)

    tstart = time.time()
    run_part_1_2(data)
    print(f'Part 1+2 finished in {time.time() - tstart} s')
    

   
                        