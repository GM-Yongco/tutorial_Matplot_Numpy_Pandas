# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

student = pd.read_csv('01_student.csv')

mark = list(student.mark)
id = list(student.id)

print(type(student))

temp = student.name
print(temp)
print(type(temp))

plt.scatter(id, mark, color = '#888', marker = 'X', s = 50)
plt.show()