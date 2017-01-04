print("hello","world")
x = 1
y = 1
z = 2
if x==y:
    print("x==y")
elif x!= y:
    print("x!=y")
else:
    print("else")
        

list = ["one","two","three"]
for num in list:
    print(num)
a = input("please input a num:")
print(a)


def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)
age = get_int("enter your age:")
print(age)
