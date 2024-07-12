# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

student = pd.read_csv('01_student.csv')

mark = list(student.mark[:-10])
id = list(student.id[:-10])

# plt.scatter(mark, id, color = '#888', marker = 'X', s = 50)
print(mark)

plt.hist(mark)
plt.hist(mark, bins=100, color = "#888")
plt.show()