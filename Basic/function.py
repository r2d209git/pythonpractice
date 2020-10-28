#function test

def add(a, b):
    return a+b

def add_choice(choice, *args):
    result = 0
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    else:
        result = 0

    return result

def dic_print(**kargs):
    for key, value in kargs.keys(), kargs.values():
        print(f"name = {key}, age = {value}")
        #print("name = {0}, age = {1}".format(key, value)
        #print("name = {name}, age = {age}".format(name = key, age = value)

def default_print(age, man=True):
    print("age = %d" %age)
    if man:
        print("man")
    else:
        print("woman")

print(add(3, 4))
print(add(a=3, b=4))

print(add_choice("add", 1, 2, 3, 4))
print(add_choice("mul", 1, 2, 3, 4))

dic_print(name = "bae", age = 44)
default_print(33)
default_print(44, False)

#변수의 함수 안 밖 변화
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

b = 1
def vartest():
    global b
    b = b + 1

vartest()
print(b)
