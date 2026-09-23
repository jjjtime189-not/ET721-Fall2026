"""
Lab 6, working with files
Joseph Ali-Shaw
September 23,2026
open() function allows user to open and write files
syntax: file_object = open("filename","mode")
common "mode" = r or w
always close() the file when is done
"""
print("\n ------Example 1: read a file ")
with open("phrases.txt", "r") as file1:
    print(file1.read(5))
    print(file1.read(7))
    print(file1.read())
print(f"Is the file closed? {file1.closed}")

print("\n ------Example 2: read a file lines")
#readline function reads a single line
#read up to 30 characters of the first line and then 5 characters of the second line
with open("phrases.txt", "r") as file1:
    print(file1.readline(30))
    print(file1.readline(5))
    print(file1.readline())

print("\n ------Example 3: read a file lines")
with open("phrases.txt", "r") as file1:
    print(file1.readlines())

print("\n ------Example 4: loop to each line in a file")
with open("phrases.txt", "r") as file1:
    filelines= file1.readlines()
    for eachline in filelines:
        print(len(eachline),end="\t")
        print(eachline.strip())

print("\n ------Example 5: write mode")
# w mode create a new file if it doesnt exist
# w mode overwrites a file if it exists
with open("lastname.txt", "w") as file:
    file.write("Python Basics for Data Science")
    file.write("Type your full name")

print("\n ------Example 6: append mode")
# a mode adds information to existing files
# if the file doesnt exist, then it will create a new file and append the new data
from datetime import datetime
with open("lastname.txt", "a") as file:
    file.write(f"\n{datetime.now()}")

print("\n ------Example 7: pandas")
#pandas is a data analysis and manipulation library built on top of NumPy
#provides data structures like Series and DataFrame
#install pandas --> pip install pandas

import pandas as pd

data = {
    'name' : ['Alice','Bob','Charlie'],
    'age' : [25,30,19]
}
df =pd.DataFrame(data)
print(df)