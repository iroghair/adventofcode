import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def signal_strength(c,x):
    cycli = [20, 60, 100, 140,180,220]
    if c in cycli:
        return [c,x]

def part1(lines):
    x = 1
    cycle = 1
    s = list()
    for line in lines:
        current_command = line.split()
        if current_command[0] == 'noop':
            s.append(signal_strength(cycle,x))
            cycle += 1
        elif current_command[0] == 'addx':
            s.append(signal_strength(cycle,x))
            cycle += 1
            s.append(signal_strength(cycle,x))
            cycle += 1
            x += int(current_command[1])
        else:
            print('Unknown case encountered')

    filtered_list = [i for i in s if i is not None]
    this_sum=0
    for n in filtered_list:
        this_sum += n[0]*n[1]
    return filtered_list, this_sum

def get_sprite(x):
    sprite = np.zeros(40)
    sprite[x-1:x+2] = 1
    return sprite

def append_sprite(the_CRT,sprite,cycle):
    the_CRT[cycle] = sprite[cycle%40]
    return the_CRT

def part2(lines):
    x = 1
    cycle = 0
    the_CRT = np.empty(240)
    for line in lines:
        current_command = line.split()
        if current_command[0] == 'noop':
            sprite = get_sprite(x)
            the_CRT = append_sprite(the_CRT,sprite,cycle)
            cycle += 1
        elif current_command[0] == 'addx':
            sprite = get_sprite(x)
            the_CRT = append_sprite(the_CRT,sprite,cycle)
            cycle += 1
            sprite = get_sprite(x)
            the_CRT = append_sprite(the_CRT,sprite,cycle)
            cycle += 1
            x += int(current_command[1])
        else:
            print('Unknown case encountered')
    
    return the_CRT

if __name__ == '__main__':
    myfile = 'input.txt'
    with open(myfile,'r') as file:
        lines = file.read().splitlines()

    print('Part 1: total signal strength: ', part1(lines))
    pt2_image = part2(lines).reshape(6,40)


    plt.imshow(pt2_image,interpolation='blackman',cmap='binary')
    plt.show()