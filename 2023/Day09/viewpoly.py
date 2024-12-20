# viewpoly.py

import matplotlib.pyplot as plt
import numpy as np

y = np.array([      4 ,     16   ,   43  ,   101 ,    217  ,   425  ,   753   , 197  ,  1691,    2110   , 2387 ,   2890 ,   5312 ,  14538  , 42415 , 115365 , 289902 , 684288,  1542307, 3358767 ,7119259])
x = np.arange(len(y))

plt.semilogy(x,y)
plt.show()