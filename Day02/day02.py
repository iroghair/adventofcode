import numpy as np

def playRound(shapes):
  # Split shapes into two elements, replace XYZ by ABC
  oppshape, myshape = shapes[0], replace[shapes[2]]
  
  # Question 2:
  # Take first, second or third letter of allshapes (i.e. A,B or C), depending
  # on combination of opponent shape and my Lose-Draw-Win indicator XYZ 
  myshape = 'ABC'[ (points[oppshape] + points[replace[shapes[2]]]) % 3]
  
  result = getResult(oppshape, myshape)
  return [points[oppshape], points[myshape]] + 3*result
  
def getResult(oppshape,myshape):
    # Result: [1 1] draw, [2 0] win player 1, [0 2] win player 2
  if oppshape==myshape:
      return np.array([1,1])
  else:
    return np.array(match[oppshape][myshape])
 
myfile = 'input.txt'

## Dictionaries!
# Game logic
match = {'A': { 'B': [0, 2], 'C': [2, 0]},
         'B': {'A': [2, 0], 'C': [0, 2]},  
         'C': {'A': [0, 2], 'B': [2, 0]}}

# Points for shapes
points = {'A': 1,'B': 2,'C': 3}

# In-line replacement of X,Y,Z for A,B,C
replace = {'X': 'A', 'Y': 'B','Z': 'C'}

# Open input
with open(myfile, 'r') as f:
  data = (f.read()).splitlines()

scores = np.array([0,0])

# Loop over rounds
for i in range(0,len(data)):
  scores = scores + playRound(data[i])

print(f'Opponent scores {scores[0]}, I score {scores[1]}')
