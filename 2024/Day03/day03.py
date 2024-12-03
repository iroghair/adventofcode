# day03.py
import re

def main(infile):
        
    with open(infile, 'r') as f:
        s_input = f.read()
    
    # Test string, uncomment to use instead of input.txt
    # s_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    mul = lambda a,b: a*b
    res = [eval(cmd) for cmd in re.findall(r'mul\(\d*,\d*\)', s_input)]
    result_1 = sum(res)
    print(f'Part 1: {result_1}')

    # Search from start until we find do or dont
    stop = min(s_input.find('do()'),s_input.find('don\'t()'))
    enabled = [s_input[:stop]]
    result_2 = 0
    
    # Find next do
    while (start := s_input.find('do()',stop)) != -1:
        stop = s_input.find('don\'t()',start)
        enabled.append(s_input[start:stop])

    for match in enabled:
        res2 = [eval(cmd) for cmd in re.findall(r'mul\(\d*,\d*\)', match)]
        result_2 += sum(res2)
    print(f'Part 2: {result_2}')

    exit()
    
    # Garbage:
    enabled1 = re.findall(r'do\(\)[\s\S]*don\'t\(\)', s_input)
    enabled2 = re.findall(r'do\(\)\S*mul\(\d*,\d*\)\S*$', s_input) 
    enabled3 = re.findall(r'^[\s\S]*don\'t\(\)', s_input)
    enabled = enabled1 + enabled2 + enabled3
    for match in enabled:
        res2 = [eval(cmd) for cmd in re.findall(r'mul\(\d*,\d*\)', match)]
        result_2 += sum(res2)
    print(f'Part 2: {result_2}')

if __name__ == "__main__":
    main("input.txt")
