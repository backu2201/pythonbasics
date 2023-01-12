'''name = ["apple", "mango", "chikki"]
name[1]
name.append("grapes")
print(name)
name.insert(2, "chinnu")
print(name)
name.pop(1)
print(name)
name.reverse()
print(name)
print(name[-2])
print(name[1:3])'''
# slicing
num = [20, 30, 50, 60, 80]
std = [[20, 30, 40], [45, 50, 60]]
print(sum(num))
print(sum(std[0]))
print(min(std))
for n in std:
    print(n)
    print(sum(n))
    print(max(n))
    print(min(n))
number = [1, 2, 4, 5, 6, 7, 9]
print(number.index(4))
for num in number:
    if (number.index(num) % 2 == 0):
        print(num * num)
tp = (10, 40, 50)
print(tp[2])
print(tp[-1])
data = {'name': 'madhu', 'num': 78, 'place': 'kadapa'}
print(data['name'])
print(data.get('contact'))
print(data.setdefault('contact', 56789))
print(data)
for i in data:
    print(i)
for i in data.values():
    print(i)
for k, v in data.items():
    print(k, v, sep=">")
data.update({'contact': 6789})
print(data)
data.pop('name')
print(data)
data.popitem()
print(data)
d = {}
print(type(d))
d = {20, 60, 80}
print(type(d))
a = {50, 70, 90}
b = {30, 90, 60}
print(a.union(b))
print(b - a)
print(a - b)
l1 = [20, 30, 90]

l2 = l1
print(l1)
l1.append(600)
print(l2)
print(id(l1))
print(id(l2))
l2 = l1.copy()  # deepcopy
# ids will be different in deepcopy compare to shallowcopy
def square(n):
    return n*n
print(square(8))
def getvalues(l):
    return sum(l),max(l)
num=[8,3,2,1]
s,m=getvalues(num)
print(s,m)
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(7))

#import Demolist as df
#print(df.fact(8))
#doing in demolist(demofunctions)
#def calculatewages(no,wages)
def calculatewages(days,wages):
    print(days*wages)
calculatewages(5,80)
def demo(*n1):
    print(n1)
demo(10,60,90)
demo(10)
def demo1(**n1):
    print(n1)
demo1(name="chinnu",age=8)
'''import os
import madhurireddy
files = os.listdir("d://chinnu")
print(files)
shutil.copytree'''
class Person:
    name="madhurireddy"
    id=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(self.name,self.id)
P=Person("madhurireddy",600)
P.show()


#iterators
l=[10,40,80,90]
s=iter(l)
print(next(s))
print(next(s))
l=[i for i in range(40)]
print(l)
def num():
    m=1
    print("first print")
    yield m
    m+=2
    print("second print")
    yield m
    m+=2
    print("third print")
    yield m
    m+=2
    print("fourth")
    yield  m
x=num()
print(next(x))
print(next(x))
print(next(x))
for p in num():
    print(p)
import time
l=[i for i in range(1000)]
start_time=time.time()
for x in l:
    print(x)
end_time=time.time()
print((end_time-start_time)*10**3)
l=[i for i in range(500)]
p=iter(l)
start_time=time.time()
for x in p:
    print(x)
end_time=time.time()
print((end_time-start_time)*10**3)
def geteven(l):
    for i in l:
        if(i%2==0):
            yield i
l=[i for i in range(100)]
x=geteven(l)
for i in x:
    print(i)
def add(x,y):
    return x+y
a=add
print(a(10,30))
def incr(x):
    return x+1
def decr(x):
    return x-1
def oper(func,n):
    r=func(n)
    return r
print(oper(incr,10))
def geteven(l):
    for i in l:
        if (i % 2 == 0):
            yield i
def getodd(l):
    for i in l:
        if(i%2!=0):
            yield i
def oper(func,l):
    r=func(l)
    return r
l = [i for i in range(100)]
x = oper(geteven,l)
x = oper(getodd,l)
for i in x:
    print(i)
def add_num(n):
    def add(x):
        return x+n
    return add

num1=add_num(10)
num2=add_num(12)
print(num1(5))
print(num2(6))
def function1(func):
    def function2():
        print("hi from function2")
        func()
    return function2
def demo():
    print("hello who are you")
f=function1(demo)
f()
#@function1 before demo#

from datetime import datetime
def get_date_time(func):
    def wrapper():
        print("Function name = "+ func.__name__)
        print(datetime.today().strftime("%Y-%M-%D %H:%M:%S"))
        func()
    return wrapper
@get_date_time
def login():
    print("login ")
login()
@get_date_time
def logout():
    print("logout ")
logout()






