# Definition: Pandas is a Python library used to organize, manipulate, 
# and analyze data in tabular form. 1)create a panda series
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

# 2)program to create a dataframe
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)
print(df)

# 3)displa first 5 rows of a dataframe
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Marks": [70, 80, 75, 90, 85, 95]
})

print(df.head())

# 4)Write a Python program to access a particular column from a DataFrame.
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print("Student names:")
print(df["Name"])

# 5)Write a Python program to calculate the average marks of students
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [80, 90, 70]
}

df = pd.DataFrame(data)

print("Average marks:", df["Marks"].mean())

# 6)Write a Python program to display the basic statistical information of a DataFrame.
import pandas as pd

data = {
    "Marks": [60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

print(df.describe())