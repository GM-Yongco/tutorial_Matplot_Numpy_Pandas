import pandas as pd



student = pd.read_csv('01_student.csv')


# basically the dot-dot stuff
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
# note: if the row has too many characters, pandas will make a slash 
# and print it on the next line

pd.set_option('display.width', 1000)

print(student)