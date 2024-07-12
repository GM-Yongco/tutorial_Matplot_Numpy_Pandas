# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

l1 = np.arange(1,10)
l2 = l1*l1
l3 = l1*3
# realization that you dont have to declare l2 as an np.array

plt.subplot(1, 2, 1)
# optional
plt.plot(l1, l2)
plt.plot(l1, l2, color = 'g', linestyle = ':', linewidth = 5)
# the first part does the lines
# the second part does the dots

plt.subplot(1, 2, 2)
plt.plot(l1, l3, color = 'r', linestyle = 'dashed', linewidth = 5)

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')


plt.title("unga bunga numbers")
plt.xlabel("sideways")
plt.ylabel("vertically challenged")
plt.grid(True)
plt.show()