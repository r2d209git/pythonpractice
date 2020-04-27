import os
from time import ctime as ct

print("Current Dir : ", os.getcwd())

files = os.listdir()
print("Dir list : ", files)
print(len(files))
print(type(files))

# print only .py file
for file in files:
    if file.endswith('.py'):
        print(file)

print("Dir list[C:] : ", os.listdir("C:/"))

print(ct())