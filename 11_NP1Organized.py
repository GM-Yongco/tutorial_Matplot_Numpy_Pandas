
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
print("Version is ", np.__version__, "\n")

print("~~~~~~~~~~~~~~~~DECLARATION~~~~~~~~~~~~~~~~")

print("\n1 Dimensional ~~~~~~~~~~~~~~~~~~")

A1 = np.array([5, 4, 3, 2, 1])
print(A1)
print(A1[1])

print("\n2 Dimensional ~~~~~~~~~~~~~~~~~~")

A2 = np.array([[5, 4, 3, 2, 1],[1, 2, 3, 4, 5]])
print("start of 1st print\n", A2 , "\n")
print("start of 2nd print\n", A2[1] , "\n")
print("start of 3rd print\n", A2[1][1] , "\n")

print("\n2D + zero ~~~~~~~~~~~~~~~~~~~~~~")

A3 = np.zeros((3,3)) 
#.zeros initialized the array with the value of zero
A3[1,1] = 8
#you can overrite an array element just like in c

print("start of 1st print\n", A3 , "\n")
print("start of 2nd print\n", A3[1] , "\n")
print("start of 3rd print\n", A3[1][1] , "\n")

# the arrays numpy basically act the same as arrays in c

print("\n0 Dimensional~~~~~~~~~~~~~~~~~~~\n")

A0 = np.array(42)
print(A0)
A0 = A0+1
print(A0)
# theres also a 0 dimentional array which is basically just the value

print("~~~~~~~~~~~~~~~~~~SPECIAL~~~~~~~~~~~~~~~~~~")

print("\nfull ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

A4 = np.full((2, 2), 69)
print(A4)
# basically np.zero but you can change the fill value

print("\nA-range ~~~~~~~~~~~~~~~~~~~~~~~")

A4 = np.arange(1, 10)
print(A4)
A4 = np.arange(10, 30, 3)
print(A4)
# numpy.arange(x, y, z)
# numpy.arange(starting value, end before it reaches this value, itterate by how much)
# z is automatically assumed to be 1 if the value is empty
# z being a negative number make an empty array
# Z being 0 creates an error

print("\nRandom ~~~~~~~~~~~~~~~~~~~~~~~")

A4 = np.random.randint(1, 10)
print(A4)

A4 = np.random.randint(11, 20, 5)
print(A4)

# numpy.random.randint(x, y, z)
# z is assumed as 1 when there is no value
# z being 0 gives and empty array
# z being a negative number gives an error
# this also shows that you can easily redeclare arrrays
# reminder that y is the exclusive cap on the array and not inclusive

print("\n3N Dimension ~~~~~~~~~~~~~~~~~~~~")

A4 = np.array([1, 2, 3, 4], ndmin=3)
print(A4)

print("\n~~~~~~~~~~~~~~~~~~DETAILS~~~~~~~~~~~~~~~~~~")

print("\nType ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(type(A1))
print(type(A2))
print(type(A3))
print(type(A4))
# as we can see, all dimensions of arrays have the same types

print("\nN Dimension ~~~~~~~~~~~~~~~~~~~~")

print(A1.ndim)
print(A2.ndim)
print(A3.ndim)
print(A4.ndim)
# we use ndim to find how many dimensions there are in the array

print("\nShape ~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(A1.shape)
print(A2.shape)
print(A3.shape)
print(A4.shape)
# as we use .shape to find the shape of the array

print("~~~~~~~~~~~~~~~~~~SPECIAL2~~~~~~~~~~~~~~~~~")

print("\nReshaping ~~~~~~~~~~~~~~~~~~~~\n")

A4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(A4, 'shape is', A4.shape)
A4.shape = (4, 2)
print(A4, 'shape is', A4.shape)

# reshaping into an invalid shape causes an error

print("\n~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")