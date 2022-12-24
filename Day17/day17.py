# blocks = list(['####', ' # \n###\n # ', '  #\n  #\n###', '#\n#\n#\n#', '##\n##'])

import numpy as np
from collections import deque
blocks = deque([np.array([[1,1,1,1]]), np.array([[0,1,0],[1,1,1],[0,1,0]]), np.array([[0,0,1],[0,0,1],[1,1,1]]), np.array([[1,1,1,1]]), np.array([[1,1],[1,1]]) ])

[print(i,'\n\n') for i in blocks]


with open('test.txt', 'r') as file:
    moves = deque([*file.read()])

moves.rotate(-1)
print(moves)