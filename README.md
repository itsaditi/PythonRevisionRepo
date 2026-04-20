
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

### Class

* [class_1.py](./oop/class_1.py)
  * Basic class definition
  * Class level attributes
  * Initializer function like constructor in Java
  * Instance method receive a specific object instance as an argument and operate on data specific to that object instance
  * Instance of class
  * `type` function to inspect object type
  * `isinstance` to compare a specific instance to a known type
  * In python, every object is a subclass of the built-in object class
* [class_2.py](./oop/class_2.py)
  * Class level attributes
  * double underscore properties are hidden from other class
  * Class Methods
  * Static methos for Singleton classes
  * Access Class Attributes
  * Use static method to access a singleton object

## Inheritance

[inheritance.py](./oop/inheritance.py)

## Abstract Base Class

[abstract_class.py](./oop/abstract_class.py)

Abstract Base Classes (ABCs) in Python serve as a design pattern for creating templates or blueprints for other classes to inherit from, characterized by two primary constraints:
* Instance Prevention: Consumers are restricted from creating instances of the base class itself, as its purpose is solely to serve as a blueprint or a collection of common attributes.
* Method Enforcement: ABCs allow developers to enforce a constraint that specific methods defined in the base class must be implemented by any inheriting subclasses.

## Multiple Inheritance

[multiple_inheritance.py](./oop/multiple_inheritance.py)

Multiple Inheritance - Classes that can inherit more than one base class

In Python, the Method Resolution Order (MRO) determines the hierarchy the interpreter follows to look up methods or attributes in a class.

#### Key Principles of MRO
* Search Direction: The lookup begins in the current class. If the attribute is not found, Python searches the parent classes in the order they are defined (from left to right).
* Order Sensitivity: Changing the order of superclasses in the class definition directly alters the resolution order. For example, if class C inherits from (A, B), A is searched before B.
* Inspection: You can view a class's specific lookup sequence by accessing the __mro__ attribute.
* The Root Class: All resolution orders eventually end at the base object class, which is the superclass for every object in Python.

#### Practical Application
* Complexity: Multiple inheritance can become complex, which is why it is used sparingly in professional projects.
* Use Case: One specific area where multiple inheritance is highly valuable is in the implementation of interfaces.

## Interface

[interface](./oop/interface.py)

In Python, interfaces can be implemented by combining multiple inheritance and abstract base classes (ABCs). While Python lacks explicit built-in language support for interfaces—unlike C# or Java—it is flexible enough to replicate the pattern.

#### Defining an Interface
* The Promise: An interface acts as a contract or promise that a class will provide specific behaviors or capabilities.
* Abstract Base Classes: To create an interface, you define a class that inherits from ABC and includes abstract methods using the @abstractmethod decorator.
* No Implementation: These interface methods remain empty; they define the name and requirement of a capability without providing the actual logic.

#### Implementing and Enforcing the Interface
* Multiple Inheritance: You can add the interface class (e.g., JSONify) to a subclass's inheritance list alongside its primary base class.
* Enforcement: Once a class inherits from an interface, it must override and implement the abstract methods. Failing to do so results in a runtime error when attempting to instantiate the class.
* Scalability: This approach avoids code duplication. Instead of adding a function like toJSON to every individual base class, you can apply the focused interface class anywhere the capability is needed.

#### Practical Benefits
* Flexibility: You can grant existing classes new capabilities without modifying their original base classes.
* Clarity: Interfaces are highly effective for declaring that a class possesses a specific, reliable capability.

## Composition

While inheritance creates hierarchies based on an "is-a" relationship, composition allows for the creation of complex objects by combining simpler ones, establishing a "has-a" relationship.

#### Inheritance vs. Composition
* Inheritance ("Is-a"): A subclass inherits all attributes and methods from a base class (e.g., a "Book" is a type of "Publication").
* Composition ("Has-a"): An object is built using other objects as components (e.g., a "Book" has an "Author" and has "Chapters").
* Combination: These concepts are not mutually exclusive; developers often use both to meet specific application needs.

![image](./assets/Screenshot%202026-04-19%20at%209.12.25 PM.png)

#### Benefits of Using Composition
* De-monolithing: It breaks down large, "monolithic" classes into smaller, distinct entities, making the code more manageable.
* Separation of Responsibilities: Each class becomes responsible for its own features. For example, the Author class handles name formatting while the Book class manages overall structure.
* Flexibility and Extensibility: Extracted classes can be reused across different parts of a program or modified independently without altering the main object’s base logic.

##  Magic Methods

Python's "magic" methods are a predefined set of methods that the language automatically associates with every class definition. By overriding these methods, developers can customize a wide range of behaviors to make custom objects act like built-in Python classes.

#### Key Capabilities of Magic Methods
* String Representation: You can customize how objects appear as strings, both for end-user display and for debugging.
* Attribute Control: Magic methods allow you to manage how object attributes are accessed, including when they are retrieved or modified.
* Expression Support: You can add capabilities that allow objects to be used in expressions, such as testing for equality ($==$) or other comparison operations like greater than ($>$) or less than ($<$).
* Callable Objects: You can make an object "callable" like a function, which often results in more concise and readable code.

#### Practical Value
* Customization: These methods provide a way to deeply customize class behavior beyond standard methods.
* Flexibility and Power: Leveraging these features is a core part of what gives Python its characteristic flexibility and programming power.

### String Representation

[magic_str.py](./oop/magic_str.py)

### Equality and comparison

[magic_eq.py](./oop/magic_eq.py)

* Note - Python doesn't do an attribute by attribute comparison on objects. It just compares two different instances to each other and sees that they're not the same object in memory and therefore they're not the same. 

### Attribute Access

[magic_attr.py](./oop/magic_attr.py)

### Callable Objects

[magic_call.py](./oop/magic_call.py)


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
