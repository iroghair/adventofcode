import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# TODO create https session with GitHub login and retrieve input data automatically
myfile = 'input.txt'

# Start with empty list of calorie packages of each elf
with open(myfile, 'r') as f:
  data = f.read().split('\n\n')

# Alternative:
# elves = [], and then use elves.append
elves = np.ndarray((len(data),),dtype=object)
total_cal = np.empty([len(data),])
for n in range(0,len(data)):
  elves[n]=(np.fromstring(data[n],sep='\n'))
  total_cal[n] = np.sum(elves[n])

# Visualise what the elves are carrying
sns.histplot(data=total_cal)
plt.show()

# Print the answer
print(f'The maximum amount of calories is {np.amax(total_cal):1} carried by elf {np.argmax(total_cal):1}')