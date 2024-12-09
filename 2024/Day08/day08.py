# day08.py
from itertools import combinations,pairwise
from typing import Any

class loc():
    def __init__(self,val) -> None:
        self.val = val
    def __sub__(self,other):
        return self.val[0] - other.val[0], self.val[1] - other.val[1]
    def __add__(self,other):
        return self.val[0] + other.val[0], self.val[1] + other.val[1]

class strgrid():
    def __init__(self,data: list[str]=[]):
        self.grid = [line.strip() for line in data]
        assert all(len(a) == len(b) for a,b in pairwise(self.grid)), 'Not implemented for non-rectangular grid'
        self.shape = (len(self.grid),len(self.grid[0]))
        
    def is_inside(self,loc):
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
    
    def shape(self):
        """Return the size of the grid as a tuple"""
        return self.shape
    
    def set(self,loc,char='#'):
        self.grid[loc[0]] = self.grid[loc[0]][:loc[1]] + char + self.grid[loc[0]][1+loc[1]:]

def parse(infile):
    with open(infile, 'r') as f:
        return strgrid(f.readlines())
        
def main():
    infile = 'test.txt'
    # infile = 'test2.txt'
    infile = 'input.txt'
    part_1 = part_2 = 0
    
    antenna_grid = parse(infile)
    antennas = {char:antenna_grid.find(char) for char in antenna_grid.chars('.')}
    antinode_grid = strgrid(['.'*antenna_grid.shape[1]]*antenna_grid.shape[0])
    # print(antinode_grid)
    antinodes_p1 = []
    antinodes_p2 = []
    
    for frequency,locations in antennas.items():
        for l in combinations(locations,2):
            step = loc(l[0]) - loc(l[1])
            
            new_pos = loc(l[1]) - loc(step)
            if antenna_grid.is_inside(new_pos):
                antinodes_p1.append(new_pos)
                while antenna_grid.is_inside(new_pos):
                    antinodes_p2.append(new_pos)
                    new_pos = loc(new_pos) - loc(step)
            
            new_pos = loc(l[0]) + loc(step)
            if antenna_grid.is_inside(new_pos):
                antinodes_p1.append(new_pos)
                while antenna_grid.is_inside(new_pos):
                    antinodes_p2.append(new_pos)
                    new_pos = loc(new_pos) + loc(step)
            
            """I don't really get why this is needed according to the description, but this puts antinodes in between antennas as well"""
            new_pos = loc(l[1]) + loc(step)
            while antenna_grid.is_inside(new_pos):
                antinodes_p2.append(new_pos)
                new_pos = loc(new_pos) + loc(step)
            
            new_pos = loc(l[0]) - loc(step)
            while antenna_grid.is_inside(new_pos):
                antinodes_p2.append(new_pos)
                new_pos = loc(new_pos) - loc(step)

    for ann in antinodes_p2:
        antinode_grid.set(ann)
    print(antinode_grid)

    # exit()
    print(set(antinodes_p1))
    part_1 = len(set(antinodes_p1))
    part_2 = len(set(antinodes_p2))

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}') # 817, 910 too low; 1319 too high

if __name__ == "__main__":
    main()