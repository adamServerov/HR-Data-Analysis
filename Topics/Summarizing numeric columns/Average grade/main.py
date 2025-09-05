# Your code here. The DataFrame is already loaded as grades

grades.reset_index(drop = True, inplace = True)
print(grades.mean(axis = 1))
