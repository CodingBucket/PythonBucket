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
````

> #### String ####
````python
s = 'string'
print(len(s))        # output: 6
print(s[0])          # output: s
print(s[-1])         # output: g
print(s[0:3])        # output: str
print(s.upper())     # output: STRING
print(s.lower())     # output: string
print(s.title())     # output: String
print(s.strip())     # removes space
print(s.find('in'))  # find part of string, output: 3
print(s.replace('s', 'r'))  # output: rtring
print('str' in s)  # output: True
print('str' not in s)  # output: False
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
