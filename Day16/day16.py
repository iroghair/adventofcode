import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from collections import deque

myfile = 'test2.txt'

with open(myfile, 'r') as file:
    lines = file.readlines()

valves = dict()
for line in lines:
    name = line.split()[1]
    flowrate = int(re.findall(r'[0-9]+',line)[0])
    coupled = re.findall(r'[A-Z][A-Z]',line.split(';')[1])
    valves[name] = {'flowrate': flowrate, 'coupled': coupled}

max_valve = len(valves)
print(f'Nodes found: {sorted(valves)}, total number: {max_valve}')
flowrate = [valves[v]['flowrate'] for v in sorted(valves)]

'valve_relief = np.zeros((max_valve,))
for i,n in enumerate(sorted([v for v in valves])):
    valves[n]['id'] = i
    valve_relief[i] = valves[n]['flowrate']
graph = np.zeros((max_valve,max_valve))
for v in sorted(valves):
    vi = int(valves[v]['id'])
    for c in valves[v]['coupled']:
        ci = int(valves[c]['id'])
        # print(f"From valve {v} (ID: {valves[v]['id']}) you can move to valve {c} (ID: {valves[c]['id']})")
        graph[vi][ci] = 1

# plt.imshow(graph)

graph = csr_matrix(graph)

# Pressure relief testing
t = 30
current_valve_name = 'AA'
dist_matrix, predecessors = dijkstra(csgraph=graph, return_predecessors=True)

while t > 0:
    projected_valve_relief = (t-dist_matrix-1) * valve_relief
    current_valve = valves[current_valve_name]['id']
    move_to = np.argsort(projected_valve_relief)[-1]
    
    # Project paths (from current valve to any other node p)
    for p in range(max_valve):
        next_valve_in_path = predecessors[current_valve][p]
        while next_valve_in_path > 0 and next_valve_in_path != current_valve:
            print(next_valve_in_path)
        # nodes = deque()
        # while 
    # for moves in move_to[-1:-4:-1]:
    #     print(moves)


    # while np.shape(move_to) > 0:
    #     if np.size(predecessors[move_to[-1]]) < t:
    #         print(f'Predecessors {move_to[-1]} will be opened')
    #     else:
    #         move_to.pop()

    

    # for v in sorted(valves):
    #     vi = int(valves[v]['id'])  
    #     # for c in valves[v]['coupled']:
    t -= 1
