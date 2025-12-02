import pathlib

def main(filename: str):
    p1 = [50]
    p2 = 50
    crosses_zero = 0
    with open(filename,'r') as f:
        data = f.readlines()

    for line in data:
        # print(line.strip())
        rot = int(line[1:])
        if line.startswith('L'):
            p2 = p1[-1]
            while rot > 100:
                crosses_zero += 1
                rot -= 100
            if p1[-1] - rot < 0 and p1[-1] != 0:
                crosses_zero += 1
            p1.append((p1[-1] - rot) % 100)
        else:
            p2 = p1[-1]
            while rot > 100:
                crosses_zero += 1
                rot -= 100
            if p1[-1] + rot > 100:
                crosses_zero += 1
            # print(f'{p2=}')
            p1.append((p1[-1] + rot) % 100)
            # p2.append((p1[-1] + int(line[1:])))
    
    print(p1.count(0))
    print(crosses_zero)
    print(p1.count(0) + crosses_zero)

if __name__ == "__main__":
    print("Program start")
    main('2025/day01/input.txt')
