import os

f = open('D:\\Python\\prj\\learnpython\\file\\buy_list.txt', 'rt')

lines = f.readlines()
print(lines)

for line in lines:
    print(line, end="")

print('\n')

for line2 in lines:
    line3 = line2.split("\n")[0]
    print(line3)

f2 = open('D:\\Python\\prj\\learnpython\\file\\write_list.txt', 'wt')
f2.write("bae\n")
f2.write("kim\n")
f2.write("oh\n")
f2.write("배영규\n")

n = 10
for i in range(1, n + 1):
    f2.write(str(i) + "\n")

f2.close()


def print_list(path):
    file1 = open('D:\\Python\\prj\\learnpython\\file\\write_list2.txt', "wt")
    for pt in os.listdir(path):
        file1.write(pt + "\n")
    file1.close()


file_path = input("your file path : ")
print_list(file_path)
