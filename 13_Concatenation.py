# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

import pandas as pd


Df1 = pd.DataFrame({
	"Name": ['Bob', 'Samantha', 'Lex'], 
	"Grades":[19, 18, 20]
    },
    index = ['a', 'c', 'z']
    )

Df2 = pd.DataFrame(
    {
	"Name": ['Bo', 'Sa', 'Le'], 
	"Grades":[19, 18, 20]
    })

print(Df1)
print(Df2)

Df1 = pd.concat([Df1, Df2])

print(Df1)

# shows u can concatenate a dictionary
new_student = ({
	"Name": 'Jules', 
	"Grades":99
    })
Df1.loc[len(Df1)] = new_student

print(Df1)
print("AAAAAAAAAAAAAAAA")
print(Df1.loc['z'])
print(Df1.loc[0:, ('Grades')])


# note: indexes with only numbers are considered ints
print(Df1.loc[["a", "c", 0], ["Name"]])