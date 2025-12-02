testdata = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def split_add(subset):
    s = list(map(int,subset.split('-')))
    s[1] += 1
    return range(*s)

def check_id_symmetry(ID):
    sID = str(ID)
    mid = len(sID)//2
    return ID if sID[:mid] == sID[mid:] else None

def check_id_repetition(ID):
    sID = str(ID)
    L = len(sID)
    for i in range(1,L//2+1):
        if sID == sID[:i]*(L//i):
            return ID
    return None

ranges = list(map(split_add, testdata.split(',')))
IDs = [result for r in ranges for num in r if (result := check_id_symmetry(num)) is not None]
print('Part 1:', sum(IDs))

IDs = [result for r in ranges for num in r if (result := check_id_repetition(num)) is not None]
print('Part 2:', sum(IDs))

