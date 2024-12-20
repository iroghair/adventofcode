from itertools import permutations,combinations_with_replacement

mystring = 'abc'

for i,set in enumerate(permutations(mystring)):
    p = 0
    for c in set:
        p += 3**i + mystring.index(c)

    print(set,p)

    