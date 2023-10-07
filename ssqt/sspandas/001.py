import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print (mydataset)
print (pd.__version__)

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[1])


a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

print()
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


print()
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print('[0]')
print (myvar.loc[0])
print('[[0]]')
print (myvar.loc[[0]])
print('[[0, 1]]')
print (myvar.loc[[0, 1]])
