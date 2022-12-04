import numpy as np
import pandas as pd

myfile = 'input.txt'

# Load data as np.array
f = np.array(pd.read_table(myfile,sep=",|-",engine='python',header=None,dtype=np.int64))

isWithinBounds = np.any([
  # Second set is within first
  np.all([f[:,0] >= f[:,2] , f[:,1] <= f[:,3]],axis=0),
  # First set is within second
  np.all([f[:,0] <= f[:,2] , f[:,1] >= f[:,3]],axis=0)]
                        ,axis=0)

print(isWithinBounds.sum())