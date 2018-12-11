> #### Variable #### 

````python
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
````

> #### String ####
````python
s = 'string'
len(s)               # out: 6
s.__len__()          # out: 6
s[0]                 # out: s
s[-1]                # out: g
s[0:3]               # out: str
s.upper()            # out: STRING
s.lower()            # out: string
s.title()            # out: String
s.strip()            # removes space
s.find('in')         # find part of string, out: 3
s.replace('s', 'r')  # out: rtring
'str' in s           # out: True
'str' not in s       # out: False
````

> #### List ####
````python
list = [1, 2, 3]
print(list)
list.append(4)
print(list)
````

> #### End of file error handle ####
````python
  while True:
      try:
          n = input()
      except EOFError:
          break
````

> #### Loop index print of list using enumerate ####
````python
  list = ['a','b','c']
  for index, i in enumerate(list):
      print(index)
````

> #### String reverse with extended slice [::] begin : end : step ####
```python
s = "123456789"
print(s[::-1])    
# Output: 987654321
```

> #### String formatting ####
```python
print("{} and {}".format("string", 1))
# string and 1
```

> #### Read file ####
```python
with open("demo.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
```

> #### Write file ####
```python
text_file = open("result.txt", "w")
text_file.write(s)
text_file.close()
```

> #### Justify / ALign (left, mid, right) ####
```python
print("{0:<10}".format("Guido"))    # 'Guido     '
print("{0:>10}".format("Guido"))    # '     Guido'
print("{0:^10}".format("Guido"))    # '  Guido   '
print("{0:.^10}".format("Guido"))   #..Guido...
print("{0:.<20} {1:.>20} {2:.^20} ".format("Product", "Price", "Sum"))
#'Product............. ...............Price ........Sum.........'
```

> #### Number print ####
```python
r = 12.99
print("%.0lf" % r) # 13
```

> #### Print variable memory location ####
```python
x = 10
print(id(x))
```

> #### Show variable type ####
```python
type(1)        # out: <class 'int'>
```

> #### To clear screen ####
```python
import os

os.system('CLS')     # For windows
os.system('clear')   # For Linux
```
