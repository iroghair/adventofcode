import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# TODO create https session with GitHub login and retrieve input data automatically
myfile = 'input.txt'

# Read data to buffer (elves are separated by double newline)
with open(myfile, 'r') as f:
  data = f.read().split('\n\n')

# We create an array-of-arrays to hold the calories of each snack
elves = np.ndarray((len(data),),dtype=object)
total_cal = np.empty([len(data)])

# Alternative to use list of lists:
# elves = []
# and then use elves.append

# Store the individual snack sizes in the arrays and the totals in another one
for n in range(0,len(data)):
  elves[n]=(np.fromstring(data[n],sep='\n'))
  total_cal[n] = np.sum(elves[n])

# Visualise what elves are carrying
sns.histplot(data=total_cal)
plt.show()

# Print the answer
print(f'The maximum amount of calories is {np.int64(np.amax(total_cal)):d} carried by elf {np.argmax(total_cal):1}')