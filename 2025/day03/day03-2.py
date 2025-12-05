import numpy as np 

def largest_digit(line: str) -> tuple:
    """
    Seeks the largest, first-occurring single digit in a string 
    Returns a tuple as (digit, index) of the digit identified.
    Note: no handling of non-digit characters. 
    """
    numbers = list(map(int,line))
    res = (-1,0)
    for i,ch in enumerate(numbers):
        if ch > res[0]:
            res = (ch,i)
            if ch == 9:
                break
    return res


def main(fname: str, length: int = 12,debug: bool = False) -> int:
    with open(fname,'r') as f:
        data = f.read().split('\n')

    dsums = []
    for line in data:
        istart = 0
        digits = []
        # Exclude the last n characters from the string, 
        # or we might find a max too far towards the end to reach to the right length
        for n in range(length-1,0,-1):
            digit,iskip = largest_digit(line[istart:-n])
            digits.append(digit)
            istart += iskip+1 
        # Including the last character cannot be done with a slicing endpoint afaik, so a separate expression
        digit,iskip = largest_digit(line[istart:])
        digits.append(digit)

        dsum = 0
        for d in digits:
            dsum = dsum*10 + d
        dsums.append(dsum)
        if debug:
            print(dsum)
    
    return sum(dsums)

if __name__ == "__main__":
    fname = "test.txt"
    fname = "input.txt"
    print(f'Part 1: {main(fname,2)}')
    print(f'Part 2: {main(fname,12)}')

