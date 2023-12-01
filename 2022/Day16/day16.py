import re
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

class Scenario:
    def __init__(self, starting_node, valve_states, 
    valve_rates, dist_matrix, predecessors, 
    has_goal=False, node_list=[], total_relief=0, visited=[], track_me=False):
        self.s0 = starting_node
        self.vstat = valve_states.copy()
        self.vrate = valve_rates.copy()
        self.dm = dist_matrix
        self.pred = predecessors
        self.has_goal = has_goal
        self.node_list = node_list
        self.n_scenarios = 4
        self.total_relief = total_relief
        self.visited = visited.copy()
        self.track_me = track_me

    def get_new_scenarios(self,time_left):
        # Init a number of possible scenario's with anticipated high pressure relief, branch from current position
        new_scenarios = []
        if not self.has_goal:
            projected_valve_relief = (time_left-self.dm[self.s0,:]) * (1-self.vstat) * self.vrate
            move_to_list = np.argsort(projected_valve_relief).tolist()
            move_to_list = [m for m in move_to_list if projected_valve_relief[m] > 0]
            for goal_node in move_to_list:
                node_list = self.get_node_list(goal_node)
                scenario = Scenario(self.s0, self.vstat, self.vrate, self.dm, self.pred, True, node_list, self.total_relief, self.visited, self.track_me)
                new_scenarios.append(scenario)
        return new_scenarios
    
    def get_node_list(self,goal_node):
        node_list = [goal_node]
        via_node = self.pred[self.s0,goal_node]
        while (via_node != self.s0):
            node_list.append(via_node)
            via_node = self.pred[self.s0,via_node]
        return node_list
        
    def has_goal_defined(self):
        return self.has_goal

    def take_step(self):
        # Wel leuk om hier ook de global path (goal nodes) en detailed path (all nodes travelled) op te slaan
        # Step 0. Relief open valves
        new_relief = np.sum((self.vstat) * self.vrate)
        self.total_relief += new_relief

        # Step 1. Go to next valve 
        if len(self.node_list) > 0:
            # New current position
            self.s0 = self.node_list[-1] 
            # Remove from queue
            self.node_list.pop()
        else:
            # Step 2. Goal node has been reached
            self.visited.append(self.s0)
            # Open valve at current pos
            self.vstat[self.s0] = 1
            self.has_goal = False

    def get_total_relief(self):
        return self.total_relief

# Input
myfile = 'test.txt'
time_left = 30
starting_node_label = 'AA'

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
valve_rates = [valves[v]['flowrate'] for v in sorted(valves)]
# valve_ids = [valves[v]['id'] for v in sorted(valves)]
# valve_relief = np.zeros((max_valve,))
for i,n in enumerate(sorted([v for v in valves])):
    valves[n]['id'] = i
    # valve_relief[i] = valves[n]['flowrate']

valve_states = np.zeros((max_valve,)) # 0: closed, 1: open

graph = np.zeros((max_valve,max_valve))
for v in sorted(valves):
    vi = int(valves[v]['id'])
    for c in valves[v]['coupled']:
        ci = int(valves[c]['id'])
        graph[vi][ci] = 1

graph = csr_matrix(graph)

# Pressure relief testing
starting_node = valves[starting_node_label]['id']
dist_matrix, predecessors = dijkstra(csgraph=graph, return_predecessors=True)

scenario_list = [Scenario(starting_node, valve_states, valve_rates, dist_matrix, predecessors)]

while time_left > 0:
    print(f'Minute {30-time_left}')
    # Get new scenarios (branches from current positions, in case finished)
    new_scenarios = [s.get_new_scenarios(time_left) for s in scenario_list]
    # Put new scenarios to list
    [scenario_list.extend(s) for s in new_scenarios]
    # Remove finalized branches
    [scenario_list.remove(s) for s in scenario_list if not s.has_goal_defined()]
    # Let all scenario's move forward
    [s.take_step() for s in scenario_list]
   
    time_left -= 1

total = [s.get_total_relief() for s in scenario_list]
print('max found: ', max(total))
print('end')
# 2233 too high
# 2085 too high

