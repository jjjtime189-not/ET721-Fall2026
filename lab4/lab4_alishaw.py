"""
Lab 4, Python data using dictionary
Joseph Ali-Shaw
September 14,2026
"""
print("------Example 1: multiconditional statements------")

age = 17
if age>18:
    print("Go to AC/DC concert")
elif age==18:
    print("Go see Pink Floyd")
else:
    print("Go see MeatLoaf")
print("Move on!")

print("------Example 2: ------")
Annie=1996
Jane=199
if Annie%4==0:
    print("Annie was born in a leap year")
elif Jane%4==0:
    print("Annie was born in a leap year")
else:
    print("Neither was born in a leap year")

print("------Example 3: ------")
age=int(input("Student's age: "))
lunch="None"
if age<9:
    lunch = "milk"
elif age>=10 and age<=14:
    lunch = "sandwich"
elif age>=15 and age>=17:
    lunch = "burger"
else:
    lunch = "out of range!"
print(f"At age {age} the food is {lunch}")

print("------Example 4: ------")
for n in range(5,10):
    print(n,end="\t")
print("Print 3,2,1")
for m in range(3,0,-1):
    print(m, end="\t")

print("------Example 5: for loop in a list ------")
dates= [1982,1980,1973]
n=len(dates)
for year in dates:
    print(year)
for y in range(n):
    print(f"year {y}= {dates[y]}")

print("------Example 6: for loop to access index and element ------")
colors = ['red','yellow','green','purple','blue']
for i,c in enumerate(colors):
    print(i, c)

print("------Example 7: while loop ------")
ratings =[5,7,5,8,9,6.2,8.8]
count = 0
index = 0
lenratings=len(ratings)
while(index > lenratings):
    if ratings[index]>=8:
        count =+ 1
    index =+1
else:
    print(f"There is/are {count} good-excellent rating/s")

print("------Example 8: functions ------")
def add(n):
    updated = n+1
    print(f"{n} added 1 = {updated}")
    return updated
m = add(6)
print(f"value of m = {m}")

print("------Example 9: functions to pass strings ------")
def con(a,b):
    return(a +' - '+ b)
print(con("Bayside","NY"))

print("------EXERCISE 1: LOOPS ------")
"""
given the list of animals, create a new list with animals whose names are made of less than 6 letters
"""
animals = ['lion','giraffe','gorilla','parrots','crocodile','deer','swan']
newanimals = []
count = 0
index = 0
for pick in animals:
    if len(pick)<6:
        newanimals.append(pick)
print(newanimals)

print("------EXERCISE 2: functions ------")
# define a function to find and retunr the average of grades in list 'grades'
grades = [65,87,95,77,35]
lengraded=len(grades)
def averager(intlist,num_of_int):
    total = 0
    for added in intlist:
        total += added
        print(total)
    average = total/num_of_int
    print(average)
averager(grades,lengraded)
    