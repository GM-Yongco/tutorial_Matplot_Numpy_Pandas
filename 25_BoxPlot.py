# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

one  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
two = np.random.randint(1, 10, 8).tolist()
thr = [6, 6, 7, 7, 8, 8, 1]

list = [one, two, thr]
print(list)

plt.subplot(1, 2, 1)
plt.boxplot(list)
plt.subplot(1, 2, 2)
plt.violinplot(list, showmedians = 1)
plt.show()

# in a box plot, the center line thingy on the box is the median
# top of the bo is the 75% and the bottom is 25%
# the other 2 lines on top and bottom are the min and max
# a weird exception to the circle in the third list tho, weirdly enuff