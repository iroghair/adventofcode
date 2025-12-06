# dayXX.py

def parse(infile: str) -> tuple:
    with open(infile, 'r') as f:
        ID_ranges = []
        
        while (line := f.readline().strip()) != '':
            ID_ranges.append(list(map(int,line.split('-'))))
            ID_ranges[-1][1] += 1 # Add one for inclusivity later on

        IDs = [int(line.strip()) for line in f.readlines()]
    return ID_ranges, IDs


def main(infile: str,debug: bool = False):
    part_1 = part_2 = 0
    ID_ranges,IDs = parse(infile)

    fresh_IDs = {ID for ID in IDs for r in ID_ranges if ID in range(*r)}
    print(fresh_IDs)
    part_1 = len(fresh_IDs)
        
    print(f'Part 1: {part_1}')

    all_valid_IDs = set()
    for r in ID_ranges:
        all_valid_IDs.update(set(range(*r)))
    part_2 = len(all_valid_IDs)
    print(f'Part 1: {part_2}')

if __name__ == "__main__":
    infile = 'input.txt'
    # infile = 'test.txt'
    main(infile)