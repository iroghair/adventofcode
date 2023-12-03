import re
import numpy as np

def import_data(infile):
    with open(infile,'r') as file:
        data = file.read().splitlines()
    return data

def track_number(data,line,col):
    start = col
    end = col
    while data[line][start-1].isnumeric():
        start -=1
    while data[line][end+1].isnumeric():
        end +=1

    partnum = data[line][start:end+1]
    data[line] = data[line][:start] + 'v'*len(partnum) + data[line][end+1:] 
    return int(partnum)

def run_part_1(data):
    mask = [np.array([y,x]) for y in range(-1,2) for x in range(-1,2) if not x==y==0]

    sum_of_parts = 0
    for r,line in enumerate(data):
        for c,chr in enumerate(line):
            if chr in special:
                for m in mask:
                    x,y = m+[c,r]
                    if data[y][x].isnumeric():
                        sum_of_parts += track_number(data,y,x)

    print(f'Part 1: {sum_of_parts}')

def run_part_2(data):
    mask = [np.array([y,x]) for y in range(-1,2) for x in range(-1,2) if not x==y==0]
    sum_gear_ratio = 0
    for r,line in enumerate(data):
        for c,chr in enumerate(line):
            if chr == '*':
                part_list = []
                for m in mask:
                    x,y = m+[c,r]
                    if data[y][x].isnumeric():
                        part_list.append(track_number(data,y,x))

                if len(part_list) == 2:
                    gear_ratio = part_list[0]*part_list[1]
                    sum_gear_ratio += gear_ratio

    print(f'Part 2: {sum_gear_ratio}')

if __name__ == '__main__':
    part1 = False
    infile = 'input.txt'
    data = import_data(infile)
    special = list('/=!@#$%^&*()-+')

    # .-Padding
    data.insert(0,'.'*(len(data[0])))
    data.append('.'*(len(data[0])))
    for i,line in enumerate(data):
        data[i] = '.' + line + '.'

    if part1:
        run_part_1(data)
    else:
        run_part_2(data)
        

   
                        