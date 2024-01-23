# 1) Classes and Methods

# OBJECTS - specific instance of a class
# INSTANCE - particular occurence of an object created from a class

# CLASS - blueprint for creating objects; defines a set of functions and attributes for objects created
# METHOD - functions defined within a class; actions that objects of the class can perform

# 2) OOP Advantages and Information Storage

# Eliminating global state; storing states (variables) in objects, rather than functions
# Instantiated objects are independent of the class

# 3/4) Four Pillars of OOP

# I: Encapsulation
# attributes (states) and methods (functions) are grouped together
# prevent unintended interference

# II: Abstraction
# model objects using classes while omitting unnecessary details
# simplify complex code by basing other classes on essential properties and behaviours

# III: Inheritance
# classes can inherit methods and variables from other classes by passing them through as a parameter
# promotes code reuse and establishes relationship between classes 

# IV: Polymorphism
# objects can be treated as instances of their parent class
# different objects can use the same function in their own way

# 5) .super() Method

# SUPER - call a method from the parent class in a class hierarchy
# when child class overwrites parent's method, .super() calls 
# the og method of the parent before adding its own info

# 6) Inheritance with Parent and Child class

# child class is allowed to assume the attributes and methods from an existing class
# promotes code reuse and modularity

# 7) Composition and Organization

# COMPOSITION - class is composed of objects of other classes, instead of being derived from them
# create relationship between classes by including instance of one class in another

# 8) Class vs Instance Variables

# CLASS - variable shared by all instances (objects) of a class
# defined within the class, but oustide of any instance method
# access with variable_name

# INSTANCE - variable specific to each instance of a class
# each instance has its own copy of the instance variable
# access with self.variable_name