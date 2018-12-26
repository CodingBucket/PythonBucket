import json
import datetime
import copy
import os

# Variable
student_count = 10
name = "hasan"

# Multiline string variable
course_name = """
aaa
bbb
ccc
"""

# Python Numbers: int, float, complex
x = 1    # int
y = 1.1  # float
z = 1j   # complex

# Multiple variable assaign
x, y = 1, 2
x = y = 1

# Data swape
s1 = 's1'
s2 = 's2'
s1, s2 = s2, s1
s1, s2    # out: ('s2', 's1')

# String
s = 'string'
len(s)               # out: 6
s.__len__()          # out: 6
s[0]                 # out: s
s[-1]                # out: g
s[0:3]               # out: str
s.upper()            # out: STRING
s.lower()            # out: string
s.title()            # out: String
s.find('in')         # find part of string, out: 3
s.replace('s', 'r')  # out: rtring
'str' in s           # out: True
'str' not in s       # out: False
s.strip()            # removes space
s.lstrip()           # Removes space from the left side of the string.
s.strip()            # Removes space from the right side of the string.
s = 'a b c'
s.split()            # out: ['a', 'b', 'c']
'1'.rjust(2)         # out: ' 1'
'1'.ljust(2)         # out: '1 '
'1'.center(3)        # out: ' 1 '
'1'.zfill(2)         # out: '01'

# bool
bool(True)  # out: True
bool(False)  # out: False
bool(0)     # out: False
bool(1)     # out: True

# End of file error handle
while True:
    try:
        n = input()
    except EOFError:
        break

# Loop index print of list using enumerate
li = ['a', 'b', 'c']
for index, i in enumerate(li):
    print(index)

# String reverse with extended slice [::] begin : end : step
s = "123456789"
print(s[::-1])   # out: 987654321

# String formatting
print("{} and {}".format("string", 1))  # string and 1

# Read file
with open("demo.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

# Write file
text_file = open("result.txt", "w")
text_file.write(s)
text_file.close()

# Justify / ALign (left, mid, right)
print("{0:<10}".format("Guido"))    # 'Guido     '
print("{0:>10}".format("Guido"))    # '     Guido'
print("{0:^10}".format("Guido"))    # '  Guido   '
print("{0:.^10}".format("Guido"))   # ..Guido...
print("{0:.<20} {1:.>20} {2:.^20} ".format("Product", "Price", "Sum"))
# 'Product............. ...............Price ........Sum.........'

# Number print
r = 12.99
print("%.0lf" % r)  # 13

# Print variable memory location
x = 10
print(id(x))

# Copy
# Shallow copy: a reference of object is copied in other object.
# Deep copy: a copy of object is copied in other object.
li3 = copy.copy(li)      # Shallow copy
li2 = copy.deepcopy(li)  # Deep copy

# To clear screen
os.system('CLS')     # For windows
os.system('clear')   # For Linux

# Fibonacci number  0 1 1 2 3 5 8 13 21
a, b = 0, 1
while b < 22:
    print(b, end=' ')
    a, b = b, a + b

# Error handling
try:
    result = a/b
except ZeroDivisionError:
    print("You cant divide by zero")
except TypeError:
    print("Data type not supported")
else:
    print(result)
finally:
    print("Inside finally")

# Iterator:
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# iteration stopped when StopIteration is raised
s = 'bangladesh'
st = iter(s)
st.__next__()  # out: b
next(st)       # out: a

# Generator


def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1


# Generator is one time object
x = gen(10)
type(x)                # <class 'generator'>
for j in x:
    print(j, end=' ')  # out: 1 2 3 4 5 6 7 8 9 10

# Generator expression
gen = (x for i in range(10))  # generator object <genexpr>
type(gen)                     # out: <class 'generator'>

# Python Casting
int(1.1)   # out: 1
float(1)   # out: 1.0
str(1)     # out: '1'

# Operator
2**3  # Exponential out: 8
7//2  # Floor out: 3

# If else
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b:
    print("a is greater than b")   # one line statement

print("A") if a > b else print("B")  # shorhand if else


# Lamda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# lam = lambda a : a + 10
# lam(2)    # out: 12
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))


# Datetime
# import datetime
x = datetime.datetime.now()
dir(x)           # shows all available methods
print(x)         # print current datetime
print(x.year)
print(x.strftime('%A'))  # print current day

x = datetime.datetime(2020, 5, 17)  # Creating date object
print(x)    # out: 2020-05-17 00:00:00


# JSON
# import json
# Convert from JSON to Python:
x = '{ "name":"John", "age":30, "city":"New York"}'  # some JSON:
y = json.loads(x)  # parse x:
print(y["age"])    # the result is a Python dictionary:
j = json.dumps(y)  # convert into JSON:

# Use the indent parameter to define the numbers of indents
json.dumps(x, indent=4)

# Use the separators parameter change the default separator
json.dumps(x, indent=4, separators=(". ", " = "))

# Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
