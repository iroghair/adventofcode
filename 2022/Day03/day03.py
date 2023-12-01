import re
import string

# Set up
myfile = 'input.txt'
matches = []
total_prio = 0
total_badge = 0
alphabet = (string.ascii_lowercase + string.ascii_uppercase)

with open(myfile, 'r') as f:
  lines = f.read().rsplit()
  # Question 1
  for line in lines:
    mid = int(len(line)/2)
    c1,c2 = line[:mid],line[mid:]
    matches.append(re.search(str('['+c1+']'),c2).group())
    total_prio = total_prio + (alphabet.find(matches[-1]) + 1)
  
  # Question 2  
  for l in range(0,len(lines),3):
    badge = re.search(str('['+lines[l+2]+']'),''.join(re.findall(str('['+lines[l]+']'),lines[l+1]))).group()
    total_badge = total_badge + (alphabet.find(badge) + 1)
    
print(f'Total number of priorities is: {total_prio:d}')
print(f'Total sum of badges is: {total_badge:d}')