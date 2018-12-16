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


# List
li = [1, 2, 3, 4]
len(li)
type(li)
li2 = list(range(5))  # out: [0, 1, 2, 3, 4]
li2 = [*range(5)]     # out: [0, 1, 2, 3, 4]
li.reverse()          # Reverse the actual list
li[::-1]              # Returns a reversed list without modifiing the actual list
li.sort()             # Sort the actual list
li.insert(0, 0)       # Insert item in specific index, insert(index, item)
li.append(4)          # Append item in the list
del li[0]             # Delete the list item
li.pop(0)             # Delete & returns the deleted list item, 0 is li index.
li.remove(1)          # Removes the element
li = li + [4]         # List concate, out: [1, 2, 3, 4]
li.extend(li2)        # li2 added in li
li.count(2)           # Count specific element
li = [1] * 3          # out: [1, 1, 1]


# List Comprehension
# Normal way
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for item in li:
    if item % 2:
        even.append(item)
print(even)              # out: [2, 4, 6, 8, 10]


# List comprehension way
even = [item for item in li if item % 2 == 0]
print(even)              # out: [2, 4, 6, 8, 10]


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
