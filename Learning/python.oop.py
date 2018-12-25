
# Clsss, Class object, Instance object


class Rectangle:
    def __init__(self):
        print("Inside init of Rectangle")

    def area(self, x):
        return x * x


class Square(Rectangle):
    side = 0

    def __init__(self, x):
        self.side = x

    def area(self):   # self is instance object
        print(self.side * self.side)
        Rectangle.area(self, self.side)


ob = Square(4)        # ob is instance object
ob.side = 10
ob.area()
print(Square.side)    # Square is class object
print(Square.area(ob))
ob.__class__          # Shows the object class


# Instance


class A:
    pass


class B(A):
    pass


a = A()           # Instance create of class A
b = B()           # Instance create of class B
a.__class__       # out: <class '__main__.A'>
b.__class__       # out: <class '__main__.B'>
isinstance(b, B)  # out: True
isinstance(b, A)  # out: True
isinstance(a, A)  # out: True
isinstance(a, B)  # out: False
issubclass(A, B)  # out: False
issubclass(B, A)  # out: True
issubclass(bool, int)  # out: True
