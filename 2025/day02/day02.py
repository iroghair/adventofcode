import numpy as np

testdata = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
""
puzzle_input = "385350926-385403705,48047-60838,6328350434-6328506208,638913-698668,850292-870981,656-1074,742552-796850,4457-6851,138-206,4644076-4851885,3298025-3353031,8594410816-8594543341,396-498,1558-2274,888446-916096,12101205-12154422,2323146444-2323289192,37-57,101-137,46550018-46679958,79-96,317592-341913,495310-629360,33246-46690,14711-22848,1-17,2850-4167,3723700171-3723785996,190169-242137,272559-298768,275-365,7697-11193,61-78,75373-110112,425397-451337,9796507-9899607,991845-1013464,77531934-77616074"

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

ranges = list(map(split_add, puzzle_input.split(',')))
IDs = [result for r in ranges for num in r if (result := check_id_symmetry(num)) is not None]
print('Part 1:', sum(IDs))

IDs = [result for r in ranges for num in r if (result := check_id_repetition(num)) is not None]
print('Part 2:', sum(IDs))

