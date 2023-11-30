# day13v2.py
from itertools import zip_longest
import time

infile = 'aoc_2022_day13_large-1.txt'

def taketwo_thenskipline(iter):
    i = 0
    while (iter):
        try:
            yield (iter[i],iter[i+1])
            i += 3
        except:
            print(f'No pair to take from anymore')
            return

def taketwo_v2(pair_list):
    pair_list_iter = iter(pair_list)
    while pair_list_iter:
        try:
            yield (next(pair_list_iter), next(pair_list_iter))
        except:
            print(f'No pair to gather anymore')
            return

def compare_lists(left,right):
    for l,r in zip_longest(left,right,fillvalue=None):
        # print(l,r)
        # Case: two integers, check if l is smaller -> True
        if all(isinstance(x,int) for x in [l,r]):
            if l==r: continue
            else: return l<r
        # Case: elements in l are exhaust -> True
        elif any(x==None for x in [l,r]): 
            return l==None
        # Case: elements l+r are lists -> recurse into lists
        elif all(isinstance(x,list) for x in [l,r]):
            out = compare_lists(l,r)
            if out == None: continue
            else: return out
        # Case: One of the elements l,r is a list -> add to list and recurse into lists
        elif any(isinstance(x,list) for x in [l,r]):
            l = l if isinstance(l,list) else [l]
            r = r if isinstance(r,list) else [r]
            out = compare_lists(l,r)
            if out == None: continue
            else: return out
        else:
            print('Edge case')
        
with open(infile,'r') as file:
    data = file.readlines()

### Part 1
# correct_pairs = []
# for i,(left,right) in enumerate(taketwo_thenskipline(data)): # Use itertools.batched??
    
#     left = eval(left)
#     right = eval(right)
#     are_in_correct_order = compare_lists(left,right)
#     if are_in_correct_order:
#         correct_pairs.append(i+1)
#     print(f'Pair: {left}\n And: {right}\n{are_in_correct_order}')

# print(correct_pairs, sum(correct_pairs))

### Part 2
tstart = time.time()
new_order = [[[2]],[[6]]]
for i,signal in enumerate(data):
    if signal == '\n': 
        continue
    else:
        signal = eval(signal)
        found = False
        j = 0
        # while not found and j<len(new_order):
        while True and j<len(new_order):
            if compare_lists(signal, new_order[j]):
                new_order.insert(j,signal)
                break
            else:
                j += 1
        
        if j == len(new_order):
            new_order.append(signal)

# Print the sorted signal
for signal in new_order:
    print(signal)

# Find the indices of divider packages
div1 = new_order.index([[2]]) + 1
div2 = new_order.index([[6]]) + 1
print(f'The decoder key is {div1}*{div2}={div1*div2}, found in {time.time()-tstart} s')