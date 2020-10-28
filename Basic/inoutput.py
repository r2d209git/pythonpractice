#input/output test
number = input("숫자를 입력하세요: ")
print(number)

for i in range(10):
    print(i, end = ' ')


f = open("D:/Python/prj/pythonpractice/Basic/file.txt", 'w')
while True:
    data = input("Input your request : ")
    if not data:
        break
    else:
        f.write(data)
f.close()

f2 = open("D:/Python/prj/pythonpractice/Basic/file.txt", 'r')
print(f2.read())
for line in f2.readlines():
    if not line:
        break
    else:
        print(line)
f2.close()