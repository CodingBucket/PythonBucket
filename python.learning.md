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

> #### End of file error handle ####

````python
  while True:
      try:
          n = input()
      except EOFError:
          break
````
> Loop index print of list using enumerate

````python
  list = ['a','b','c']
  for index, i in enumerate(list):
      print(index)
````
> String reverse with extended slice [::] begin : end : step
```python
s = "123456789"
print(s[::-1])    
# Output: 987654321
```
> String formatting
```python
print("{} and {}".format("string", 1))
# string and 1
```
> Read file
```python
with open("demo.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
```
> Write file
```python
text_file = open("result.txt", "w")
text_file.write(s)
text_file.close()
```

> Justify / ALign (left, mid, right)
```python
print("{0:<10}".format("Guido"))    # 'Guido     '
print("{0:>10}".format("Guido"))    # '     Guido'
print("{0:^10}".format("Guido"))    # '  Guido   '
print("{0:.^10}".format("Guido"))   #..Guido...
print("{0:.<20} {1:.>20} {2:.^20} ".format("Product", "Price", "Sum"))
#'Product............. ...............Price ........Sum.........'
```

> Number print
```python
r = 12.99
print("%.0lf" % r) # 13
```
