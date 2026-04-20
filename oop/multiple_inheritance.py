"""
Multiple Inheritance - Classes that can inherit more than one base class
"""

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

"""
Changing the order of superclasses in the class definition directly alters the resolution order. 
For example, if class C inherits from (A, B), A is searched before B.
"""
class C(A, B):
    def __init__(self):
        super().__init__()
    
    def show_props(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name) # Prints Class A due to C(A, B)


c = C()
print(C.__mro__) # Prints Resolution Order
c.show_props()