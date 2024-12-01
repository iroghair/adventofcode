# day01.py

import numpy as np

def load_txt():
    return np.loadtxt(fname='input.txt')
    
def main():
    array = load_txt()
    A = np.sort(array,axis=0)
    
    # Part 1
    distances = np.abs(A[:,0] - A[:,1])
    print(f'Part 1: {int(sum(distances))}')
    
    # Part 2
    values,counts = np.unique(array[:,0],return_counts=True)
    similarities = [v*c*np.sum(A[:,1]==v) for v,c in zip(values,counts)]
    print(f'Part 2: {int(np.sum(similarities))}')
    
if __name__ == "__main__":
    main()