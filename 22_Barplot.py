# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

student = pd.read_csv('01_student.csv')

names = list(student.name[0:10])
mark = list(student.mark[0:10])

print(type(student))

temp = student.name
print(temp)
print(type(temp))

plt.subplot(2, 1, 1)
plt.bar(names, mark)

plt.subplot(2, 1, 2)
plt.barh(names, mark, color = 'orange')

plt.show()