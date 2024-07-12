# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd

# MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Version is ", pd.__version__, "\n")

Df1 = pd.DataFrame({
                "Name": ['Bob', 'Samantha', 'Lex'], 
                "Grades":[19, 18, 20]
                })
print(Df1)
# dataframes are made from dictionaries
# keys, ie. "Name" and "Grades", become columns
# values become the rows

student = pd.read_csv('01_student.csv')
print("\n\nCSV ----------------- \n\n",student.shape, 
        "\n\nspace :DDD\n\n", student.head(10), 
        "\n\nspace :DDD\n\n", student.tail(3), 
        "\n\nspace :DDD\n\n", )

print("\n\n ------------ SPACEEEEEEEEEE1 ------------- \n\n")
print(student.describe())


print("\n\n ------------ SPACEEEEEEEEEE2 ------------- \n\n")
# extrating specific rows and columns in a dataframe
# .iloc[list of, list of columns]
# you can use a range if u want tho

print(student.iloc[0:20, [2,3]])

print("\n\n ------------ SPACEEEEEEEEEE3 ------------- \n\n")
# extrating specific rows and columns in a dataframe
# .iloc[list of, list of columns]
# you can use a range if u want tho

print(student.iloc[0:20 , 1:4])
print(student.loc[0:20 , ('id', 'name', 'mark')])

print("\n\n ------------ SPACEEEEEEEEEE4 ------------- \n\n")

print(student.head(10))
student = student.drop('gender', axis=1)
print(student.head(10))
student = student.drop( [2, 4], axis=0)
print(student.head(10))

# axis 0 tells the computer to remove a row in index 2
# axis 1 tells the computer to remove the column named 'gender'