import re

infile = 'input.txt'
part2 = True

with open(infile, 'r') as file:
    data = file.read().splitlines()


# Create replacement dictionary
ddict = {}
for digit,word in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
    ddict[word]=digit

sum_of_values = 0

for line in data:
    if part2:
        # Find occurrences of word-digits
        replace_index = []
        for word,digit in ddict.items():
            for m in re.finditer(word,line):
                idx = m.start(0)
                replace_index.append((idx,digit,word))
        replace_index.sort()

        # Replace last and first words with actual digits
        if replace_index:
            i = replace_index.pop(-1)
            line = line[:i[0]] + str(i[1]) + line[i[0]:]
        while replace_index:
            i = replace_index.pop(0)
            line = line[:i[0]] + str(i[1]) + line[i[0]:]

    # Match actual digits and select first and last to create a number
    digits = re.findall('\d',line)
    calibration_value = int(digits[0]+digits[-1])
    sum_of_values += calibration_value

print(f'Sum of values: {sum_of_values}')

