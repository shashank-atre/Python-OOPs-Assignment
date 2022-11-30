# Q1. What is the purpose of Python's OOP?
# Answer--> In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
#It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
#The main concept of OOPs is to bind the data and
#the functions that work on that together as a single unit so that no other part of the code can access this data.

# Q2. Where does an inheritance search look for an attribute?
# Answer--> An inheritance search looks for an attribute first in the instance object,
#then in the class the instance was created from, then in all higher superclasses, progressing from left to right (by default).
#The search stops at the first place the attribute is found.

# Q3. How do you distinguish between a class object and an instance object?
# Answer--> A class is a template for creating objects in a program, whereas the object is an instance of a class.
#A class is a logical entity, while an object is a physical entity

# Q4. What makes the first argument in a class’s method function special?
# Answer--> Self is the first argument to be passed in Constructor and Instance Method.
#Self must be provided as a First parameter to the Instance method and constructor.
#If you don't provide it, it will cause an error.

# Q5. What is the purpose of the init method?
# Answer--> The __init__ method lets the class initialize the object's attributes and serves no other purpose.
#It is only used within classes.

# Q6. What is the process for creating a class instance?
# Answer--> To create instances of a class, you call the class using class name and
#pass in whatever arguments its __init__ method accepts.

# Q7. What is the process for creating a class?
# Answer--> To create a class, use the keyword class.
#ex--
class MyClass:
  x = 5

print(MyClass)

# Q8. How would you define the superclasses of a class?
# Answer--> The class from which a class inherits is called the parent or superclass.

# Q9. What is the relationship between classes and modules?
# Answer--> Modules are collections of methods and constants. They cannot generate instances.
#Classes may generate instances (objects), and have per-instance state (instance variables). 

# Q10. How do you make instances and classes?
# Answer--> To create instances of a class, you call the class using class name and pass in whatever arguments
# its __init__ method accepts.To create a class, use the keyword class.

# Q11. Where and how should be class attributes created?
# Answer--> A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.
# Use class_name.class_attribute or object_name.class_attribute to access the value of the class_attribute.
# Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.

# Q12. Where and how are instance attributes created?
# Answer--> An instance attribute is a Python variable belonging to only one object.
# It is only accessible in the scope of the object and it is defined inside the constructor function of a class.
# For example, __init__(self,..)

# Q13. What does the term "self" in a Python class mean?
# Answer--> self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in python.
#It binds the attributes with the given arguments. The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes

# Q14. How does a Python class handle operator overloading?
# Answer--> Python operators work for built-in classes. But the same operator behaves differently with different types.
# For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

# Q15. When do you consider allowing operator overloading of your classes?
# Answer--> The operator overloading in Python means provide extended meaning beyond their predefined operational meaning.
# Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists.
# We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.

# Q16. What is the most popular form of operator overloading?
# Answer--> A very popular and convenient example is the Addition (+) operator.
#Just think how the ‘+’ operator operates on two numbers and the same operator operates on two strings. 
#It performs “Addition” on numbers whereas it performs “Concatenation” on strings.
#Operators in Python work for built-in classes, like int, str, list, etc.
#But you can extend their operability such that they work on objects of user-defined classes too.

# Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
# Answer--> Inheritance and Polymorphism are the two most important concepts to grasp in order to comprehend Python OOP code.

# Q18. Describe three applications for exception processing
# Answer--> 

# Q19. What happens if you don't do something extra to treat an exception?
# Answer--> if you don't handle exceptions
#When an exception occurred, if you don't handle it,
#the program terminates abruptly and the code past the line that caused the exception will not get executed.

# Q20. What are your options for recovering from an exception in your script?
# Answer--> We can also provide a generic except clause, which handles any exception.

# Q21. Describe two methods for triggering exceptions in your script.
# Answer--> The two methods to handle Python exceptions: Try – This method catches the exceptions raised by the program.
# Raise – Triggers an exception manually using custom exceptions.

# Q22. Identify two methods for specifying actions to be executed at termination time,
# regardless of whether or not an exception exists.
# Answer--> 

# Q23. What is the purpose of the try statement?
# Answer--> The try block lets you test a block of code for errors.

# Q24. What are the two most popular try statement variations?
# Answer--> There are two other optional segments to a try block: else and finally .
# Both of these optional blocks will come after the try.

# Q25. What is the purpose of the raise statement?
# Answer--> The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# Q26. What does the assert statement do, and what other statement is it like?
# Answer--> The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True,
# if not, the program will raise an AssertionError.

# Q27. What is the purpose of the with/as argument, and what other statement is it like?
# Answer--> n Python, with statement is used in exception handling to make the code cleaner and much more readable.
# It simplifies the management of common resources like file streams.

# Q28. What are *args, **kwargs?
# Answer--> We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
# Python has *args which allow us to pass the variable number of non keyword arguments to function.
# **kwargs allows us to pass the variable length of keyword arguments to the function.

# Q29. How can I pass optional or keyword parameters from one function to another?
# Answer--> Users can either pass their values or can pretend the function to use theirs default values which are specified.

# In this way, the user can call the function by either passing those optional parameters or just passing the required parameters. 
# There are two main ways to pass optional parameters in python 
# 1. Without using keyword arguments.
# 2. By using keyword arguments.

# Q30. What are Lambda Functions?
# Answer--> Python Lambda Functions are anonymous function means that the function is without a name.
# As we already know that the def keyword is used to define a normal function in Python.
# Similarly, the lambda keyword is used to define an anonymous function in Python.

# Q31. Explain Inheritance in Python with an example?
# Answer--> One of the core concepts in object-oriented programming (OOP) languages is inheritance.
# It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.
# Inheritance is the capability of one class to derive or inherit the properties from another class.

# Q32. Suppose class C inherits from classes A and B as class C(A,B).
# Classes A and B both have their own versions of method func().
# If we call func() from an object of class C, which version gets invoked?
# Answer--> 

# Q33. Which methods/functions do we use to determine the type of instance and inheritance?
# Answer--> Using isinstance() function, we can test whether an object/variable is an instance of the specified type or class such as int or list. 
# In the case of inheritance,we can checks if the specified class is the parent class of an object.

# Q34.Explain the use of the 'nonlocal' keyword in Python.
# Answer--> The nonlocal keyword is used to work with variables inside nested functions, 
# where the variable should not belong to the inner function.
# Use the keyword nonlocal to declare that the variable is not local.

# Q35. What is the global keyword?
# Answer--> A global keyword is a keyword that allows a user to modify a variable outside the current scope.
# It is used to create global variables in Python from a non-global scope, i.e. inside a function.
# Global keyword is used inside a function only when we want to do assignments or when we want to change a variable.
# Global is not needed for printing and accessing