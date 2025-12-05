import numpy as np 

def largest_digit(line: str):
    """
    Seeks the largest single digit in a string within a given range. 
    Returns a tuple as (digit, index) of the digit identified. 
    """
    numbers = list(map(int,line))
    res = (-1,0)
    for i,ch in enumerate(numbers):
        if ch > res[0]:
            res = (ch,i)
            if ch == 9:
                break
    return res


def main(fname: str, length: int = 12):
    with open(fname,'r') as f:
        data = f.read().split('\n')

    dsums = []
    for line in data:
        istart = 0
        digits = []
        for n in range(length-1,0,-1):
            digit,iskip = largest_digit(line[istart:-n])
            digits.append(digit)
            istart += iskip+1 
        digit,iskip = largest_digit(line[istart:])
        digits.append(digit)
            
        dsum = 0
        for d in digits:
            dsum = dsum*10 + d
        dsums.append(dsum)
        print(dsum)
    
    print(sum(dsums))

if __name__ == "__main__":
    fname = "test.txt"
    fname = "input.txt"
    main(fname,12)

