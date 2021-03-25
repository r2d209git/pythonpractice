#input/output test
number = input("숫자를 입력하세요: ")
print(number)

for i in range(10):
    print(i, end = ' ')

print("\n write to file")
f = open("D:/Python/prj/pythonpractice/Basic/file.txt", "w")
while True:
    data = input("Input your request : ")
    if not data:
        break
    else:
        f.write(data + "\n")
f.close()

print("\n read from file - whole")
f2 = open("D:/Python/prj/pythonpractice/Basic/file.txt", 'r')
print(f2.read())
f2.close()

print("\n read from file - list line")
f3 = open("D:/Python/prj/pythonpractice/Basic/file.txt", 'r')
for line in f3.readlines():
    if len(line) == 0:
        break
    else:
        print(line)
f3.close()

print("\n read from file - line by line")
f4 = open("D:/Python/prj/pythonpractice/Basic/file.txt", 'r')
while True:
    data = f4.readline()
    if not data:
        break
    else:
        print(data)
f4.close()