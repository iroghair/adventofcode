import re

part1 = False
infile = 'input.txt'
RGBmatch = (12,13,14)
set_power = []

with open(infile,'r') as file:
    data = file.read().splitlines()

sum_IDs = 0
for line in data:
    header_sets = line.split(':')
    game = int(header_sets[0].split()[1])
    print('Game', game)
    sum_IDs += game
    RGBmax = [0,0,0]
    for set in header_sets[1].split(';'):
        # print(set)
        reds = re.findall(r'\d+\sred',set)
        greens = re.findall(r'\d+\sgreen',set)
        blues = re.findall(r'\d+\sblue',set)
        RGBset = (int(reds[0].split()[0]) if (reds) else 0,\
                    int(greens[0].split()[0]) if (greens) else 0, \
                    int(blues[0].split()[0]) if (blues) else 0)

        if (part1):
            if any(i>j for i,j in zip(RGBset,RGBmatch)):
                print('Set: ', set, ' (RGB: ', RGBset, ' does not fit ')
                sum_IDs -= game
                break
        else:
            RGBmax = [max(i,j) for i,j in zip(RGBmax,RGBset)]
            print(f'RGBmax: {RGBmax}, RGBset: {RGBset}')
    set_power.append(RGBmax[0]*RGBmax[1]*RGBmax[2])
    print(f'Game: {game} has power {set_power}')
    
if (part1):    
    print(sum_IDs)
else:
    print(f'The total of the set powers is {sum(set_power)}')        
