# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from ZZ_PandaHeader import *
import pandas as pd

# MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Version is ", pd.__version__, "\n")

l1 = [1, 2, 3, 4, 5]

# apparently you can imput a list into a serires and I think it should work in numpy as well

s1 = pd.Series(l1)
print(s1)
print(type(s1))

# what is printed is the index and the element
# it also gives the type which is a 64 bit integer

s1[3] = 69
print(s1)

s2 = pd.Series([6, 7, 8, 9, 0], index=['a', 'sparta', 'c', 'd', 'e'])
print(s2)
s2['sparta'] = 21
print(s2)


# panda series as dictionaries
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
s3 = pd.Series(dict1)
print(s3)

s4 = pd.Series(dict1, index={'a', 'z', 'e', 'f'})
print(s4)
print("COLON THINGY ~~~~~~~~~~~~~~~~~~~~~")
print(s3[:5])
print(s3['d':])
print(s3[:-3])
print(s3[-3:])

print("\n\n\n\nSCALAR VALUES ~~~~~~~~~~~~~~~~~~~~~")

li = [1, 2, 3, 4, 5]
s1 = pd.Series(li)
s1 += 5

print(s1)

s2 = pd.Series([90, 90, 90, 90, 90])
s2 += s1
print(s2)

print(s1*5)
print(s1)