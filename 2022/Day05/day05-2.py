import re
myfile = 'input.txt'

with open(myfile,'rt') as f:
  lines = f.read().splitlines()

hasInit = False  # Whether to do the initialisation
for line,n in zip(lines,range(len(lines))):
  moveList = [int(x) for x in re.findall(r'\d+',line)]
  # Mooier: 
  # _,amount,_,van,_,naar = line.strip().split(" ")
  if (hasInit and moveList):
    [Nc,Fr,To] = moveList
    Fr=Fr-1
    To=To-1
    stack[To].extend(stack[Fr][-1:-Nc-1:-1][::-1])
    del stack[Fr][-1:-Nc-1:-1]
    # print(stack)
  
  # Find container numbers  
  # Read the container stacks when the stack numbers are recognized
  elif (line.lstrip().rstrip().startswith('1') and not hasInit):
    # Count the number of stacks
    totalStacks = len(line.lstrip().rstrip().split())
    stack = [[] for i in range(totalStacks)]
    # Fill the lists (1 per stack) from bottom to top (top of list is ground floor)
    for nStack in range(totalStacks):
      for hStack in range(n,0,-1):
        stack[nStack].append(lines[hStack-1][line.find(str(nStack+1))].strip())
      stack[nStack] = [x for x in stack[nStack] if x != '']
    filter(None, stack)
    hasInit=True
    # print(stack)
  
print(''.join([x[-1] for x in stack]))