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

    ID_range_list_changed = True
    while ID_range_list_changed:
        ID_range_list_changed = False
        ID_ranges.sort(key=lambda x: x[0])
        for i,r in enumerate(ID_ranges.copy()):
            for r2 in ID_ranges.copy()[:i]:
                # Check whether the starting point of a range lies inside another range
                if r[0] < r2[-1]:
                    ID_ranges.insert(i,[min(r[0],r2[0]),max(r[-1],r2[-1])])
                    ID_ranges.remove(r)
                    ID_ranges.remove(r2)
                    ID_range_list_changed = True
                    break
            if ID_range_list_changed:
                break
    print(ID_ranges)
    print(sum([r[-1]-r[0] for r in ID_ranges]))

        
# ....xxxx.x.....xxxxxxxxAAAAAA...xxxxxxx...xxxxxxxxxxxxxxxxxxxxxxxAAAAAAAAAAAxxxx...xxxxxxxxxxxxxxxxxx
if __name__ == "__main__":
    infile = 'input.txt'
    # infile = 'test.txt'
    main(infile)