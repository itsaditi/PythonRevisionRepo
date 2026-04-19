
# Useful commands

### Command to create virtual env
```python
python3 -m venv .venv
```

### Command to run virtual env
```python
source venv/bin/activate
```

# Basic

* [variables.py](./variables.py)
* [math.py](./math.py)
* [conditions.py](./conditions.py)

## Datastructures
* [list.py](./datastructures/list.py)
* [tuple.py](./datastructures/tuple.py)
* [dictionary.py](./datastructures/dictionary.py)
* [stack.py](./datastructures/stack.py)
  * Using Doubly Ended Queue
* [queue.py](./datastructures/queue.py)
  * Using Doubly Ended Queue
  * Using List
* [set.py](./datastructures/set.py)

# OOP Refresher

## Class

* A class is a collection of objects. 
* Classes are blueprints for creating objects. 
* A class defines a set of attributes and methods that the created objects (instances) can have

## Objects

* An Object is an instance of a Class. 
* It represents a specific implementation of the class and holds its own data. 
* An object consists of:

  * State: It is represented by the attributes and reflects the properties of an object.
  * Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
  * Identity: It gives a unique name to an object and enables one object to interact with other objects.


| Term | Definition | 
|---|---|
| Class | Collection of objects, A blueprint for creating objects of particular type. A class defines a set of attributes and methods that the created objects (instances) can have |
| Methods | Regular functions that are part of a class |
| Attributes | Variables that hold data that are part of a class |
| Object | Specific instance of a class |
| Inheritance | Means by which class can inherit capabilities from another |
| Composition | Means of building complex obj out of other objects |

## Four Pillars of OOP

### Inheritance

Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

### Polymorphism

* Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different types to be treated as objects of a common super type. 
* This enables a single interface to work with various data types, making code easier to write and maintain.

#### Types of Polymorphism

* Compile-time Polymorphism (Static Polymorphism)
  * Method Overloading: Multiple methods in the same class can have the same name but different parameters. The method to be executed is determined at compile time based on the method signature.
* Runtime Polymorphism (Dynamic Polymorphism)
  * Method Overriding: A subclass can provide a specific implementation of a method that is already defined in its superclass. The method to be executed is determined at runtime, allowing for more flexible code.

### Encapsulation

* Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. 
* A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

### Abstraction

* Abstraction hides the internal implementation details while exposing only the necessary functionality. 
* It helps focus on "what to do" rather than "how to do it."

## Basic

* [class_1](./oop/class_1.py)
  * Basic class definition
  * Class level attributes
  * Initializer function like constructor in Java
  * Instance method receive a specific object instance as an argument and operate on data specific to that object instance
  * Instance of class
  * `type` function to inspect object type
  * `isinstance` to compare a specific instance to a known type
  * In python, every object is a subclass of the built-in object class
* [class_2](./oop/class_2.py)
  * Class level attributes
  * double underscore properties are hidden from other class
  * Class Methods
  * Static methos for Singleton classes
  * Access Class Attributes
  * Use static method to access a singleton object



# Naming conventions 

## Underscores in Naming Conventions

### Single Leading Underscore (`_name`)

This is a naming convention to indicate that a variable, function, or method is intended for internal use (non-public) within a module or class. Python does not strictly enforce this, but it serves as a hint to other programmers and prevents the name from being imported by a wildcard import (from module import *).

### Single Trailing Underscore (`name_`): 

This convention is used to avoid naming conflicts with Python keywords or built-in names. For example, you can use class_ as a variable name instead of class, which is a reserved keyword.

### Double Leading Underscore (`__name`): 
When used within a class definition, this triggers a language feature called name mangling. The Python interpreter automatically changes the name to `_ClassName__name` to help prevent accidental overriding of attributes in subclasses. It does not create a truly "private" variable, as the mangled name can still be accessed directly.


### Double Leading and Trailing Underscore :

These are special methods, often referred to as "dunder" (double underscore) or "magic" methods, that have specific functionality defined by the Python language. Examples include `__init__`, `__str__`, and `__len__`. You should avoid using this naming scheme for your own attributes to prevent conflicts with future Python language features
