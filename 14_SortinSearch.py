# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
import pandas as pd



student = pd.read_csv('01_student.csv')
student = student.sort_values(by = 'mark',      #which colum to sort by
                              axis = 0,         #specifies to sort row
                              ascending = True) #ascending or descending
# print(student)



# student = student.where(student['gender'] == 'male')
index_def = student[student['gender'] == 'female'].index
print(index_def)



# drops the indexes where the value in gender is female
student = student.drop( index_def, axis=0)
print(student)

if 'Gimmy' in student['name'].values:
    print("there is a Jimmy")
else:
    print("there is no Jimmy")

print(student.loc[student[student['name'] == 'Gimmy'].index])