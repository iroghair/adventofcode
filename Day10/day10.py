def signal_strength(c,x):
    cycli = [20, 60, 100, 140,180,220]
    if c in cycli:
        return [c,x]

if __name__ == '__main__':
    myfile = 'input.txt'
    with open(myfile,'r') as file:
        lines = file.read().splitlines()

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
    print(filtered_list, this_sum)
