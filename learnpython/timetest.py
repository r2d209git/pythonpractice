import time
print(time.time())

cur_time = time.ctime()

print(time.ctime())

print("Year : " + time.ctime().split(" ")[-1])

n = 10
for i in range(1, n+1):
    if i != n:
        print(i, end=", ")
    else:
        print(i)
        print("Count end!")
        break
    time.sleep(1)

