
# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from PY1_Header import *
import numpy as np
# the 'as' part is just giving it an alias, 
# and we can just numpy.whatever if we wated to
# its worth noting that if an alias is setup
    # numpy.whatever wont work and the alias should be used

# MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~\n")

print(np.__version__)

print("\n1 Dimentional~~~~~~~~~~~~~~~~~~~\n")

A1 = np.array([5, 4, 3, 2, 1])

printf(A1)
printf(type(A1))
printf(A1[1])

print("\n2 Dimentional~~~~~~~~~~~~~~~~~~~\n")

A2 = np.array([[5, 4, 3, 2, 1],[1, 2, 3, 4, 5]])

print(A2)
printf(type(A2)) 
printf(A2[1])
printf(A2[1][1])

# so basically works the same as an array in C
# we can also see that the arrays have the same type

print("\n2 Dimentional agen~~~~~~~~~~~~~~\n")

A3 = np.zeros((3,3)) #.zeros initialized the array with the value of zero
A3[1,1] = 8
print(A3)
print('shape: ', A3.shape)
print(A3.ndim)
print(A1.ndim)

# we can also redeclare a value within an array just like in C
# and additionally check how many dimentions within an array

print("\n0 Dimentional~~~~~~~~~~~~~~~~~~~\n")

A0 = np.array(42)
print(A0)
A0 = A0+1
print(A0)
print(A0.ndim)
# theres also a 0 dimentional array which is basically just the value

print("\n3 Dimentional~~~~~~~~~~~~~~~~~~~\n")

A4 = np.array([1, 2, 3, 4], ndmin=3)
print(A4)
print('number of dimensions :', A4.ndim)
print('shape: ', A4.shape)

# giving details about the array

A5 = np.array([[[1, 2, 3]]])
A5[0, 0, 1] = 7
print(A5)
# you can make multidimentional arrays with empty sub arrays?

print("\nN Dimentional~~~~~~~~~~~~~~~~~~~\n")

A6 = np.full((2, 2), 69)
print(A6)
# basically np.zero but you can change the fill value

print("\nA-range ~~~~~~~~~~~~~~~~~~~\n")

A7 = np.arange(1, 10)
print(A7)

A8 = np.arange(10, 30, 3)
print(A8)

# numpy.arange(x, y, z)
# numpy.arange(starting value, end before it reaches this value, itterate by how much)
# z is automatically assumed to be 1
# z being a negative number make an empty array
# Z being 0 creates an error

print("\nrandom ~~~~~~~~~~~~~~~~~~~\n")

A1 = np.random.randint(1, 10)
print(A1)

A1 = np.random.randint(11, 20, 5)
print(A1)

# numpy.random.randint(x, y, z)
# z is assumed as 1 when there is no value
# z being 0 gives and empty array
# z being a negative number gives an error
# this also shows that you can easily redeclare arrrays
# reminder that y is the exclusive cap on the array and not inclusive

print("\nreshaping ~~~~~~~~~~~~~~~~~~~\n")

A1 = np.array([1, 2, 3, 4], ndmin = 2)
print(A1, 'shape is', A1.shape)
A1.shape = (2, 2)
print(A1, 'shape is', A1.shape)

# reshaping into an invalid shape causes an error

print("\n~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")