import re

infile = 'input.txt'
RGBmatch = (12,13,14)

with open(infile,'r') as file:
    data = file.read().splitlines()

sum_IDs = 0
for line in data:
    header_sets = line.split(':')
    game = int(header_sets[0].split()[1])
    print('Game', game)
    sum_IDs += game
    for set in header_sets[1].split(';'):
        # print(set)
        reds = re.findall(r'\d+\sred',set)
        greens = re.findall(r'\d+\sgreen',set)
        blues = re.findall(r'\d+\sblue',set)
        RGBset = (int(reds[0].split()[0]) if (reds) else 0,\
                    int(greens[0].split()[0]) if (greens) else 0, \
                    int(blues[0].split()[0]) if (blues) else 0)

        if any(i>j for i,j in zip(RGBset,RGBmatch)):
            print('Set: ', set, ' (RGB: ', RGBset, ' does not fit ')
            sum_IDs -= game
            break
        
print(sum_IDs)
        
        # greens = re.search(r'\d+\sgreen',set)[0].split()[0]
        # blues = re.search(r'\d+\sblue',set)[0].split()[0]
        # rgbset=(reds,0,0)
        # print(rgbset)
    # b = re.split(r'\b.*;',line)
    # print(b)
