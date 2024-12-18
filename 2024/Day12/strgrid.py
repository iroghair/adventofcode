# strgrid.py
from itertools import pairwise
class loc():
    def __init__(self,val) -> None:
        self.val = [None,None]
        self.val[0] = val[0]
        self.val[1] = val[1]
        
    def __eq__(self,other):
        return all([int(i) == int(j) for i in self.val for j in other.val])
    
    def __sub__(self,other):
        return self.val[0] - other.val[0], self.val[1] - other.val[1]
    
    def __add__(self,other):
        return self.val[0] + other.val[0], self.val[1] + other.val[1]
    
    def __str__(self):
        return str(self.val[0]) + ', ' + str(self.val[1])
        
class strgrid():
    def __init__(self,data=None,shape=None):
        if isinstance(data, list):
            self.create_from_list(data)
        elif isinstance(shape,tuple) or isinstance(shape,list):
            self.create_from_shape(shape)
            
    def create_from_shape(self,shape:list) -> None:
        assert len(shape) == 2, 'Not implemented for other than 2D grids (shape should contain exactly 2 numbers)'
        self.grid = ['.'*shape[1] for row in range(shape[0])]
        self.shape = (shape[0], shape[1])
    
    def create_from_list(self,data) -> None:
        self.grid = [line.strip() for line in data]
        assert all(len(a) == len(b) for a,b in pairwise(self.grid)), 'Not implemented for non-rectangular grid'
        self.shape = (len(self.grid),len(self.grid[0]))
        
    def __getitem__(self,idx):
        assert self.is_inside(idx), f'Indices {idx} outside of range'
        return self.grid[idx[0]][idx[1]]
    
    def __setitem__(self,idx, char: str):
        assert self.is_inside(idx), f'Indices {idx} outside of range'
        self.set(idx,char)
            
        
    def get_locations(self):
        return [(x,y) for x in range(self.shape[0]) for y in range(self.shape[1])]
        
    def is_inside(self,loc: list) -> bool:
        return 0 <= loc[0] < self.shape[0] and 0 <= loc[1] < self.shape[1]
        
    def chars(self,exclude=''):
        """Find all characters in string grid with the exception of the given characters"""
        return set([char for line in self.grid for char in line if char not in exclude])
    
    def find(self,char):
        """Find all (row,col) indices in a grid of strings"""
        return [(r,p) for r,line in enumerate(self.grid) for p in [pos for pos,c in enumerate(line) if c == char]]
        
    def __str__(self) -> str:
        """Print the grid as a string"""
        return '\n'.join(self.grid)
    
    def get_shape(self) -> tuple:
        """Return the size of the grid as a tuple"""
        return self.shape
    
    def set(self,loc,char='#'):
        self.grid[loc[0]] = self.grid[loc[0]][:loc[1]] + char + self.grid[loc[0]][1+loc[1]:]