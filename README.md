# Multilevel_Inheritance

Multilevel Inheritance is also possible in Python.

Multilevel Inheritance: It is a mechanism through which features of the base class and the derived class are inherited into a new derived class. It is like the grandparent-parent-child relationship. This kind of inheritance can go upto any level.




Syntax:
class BaseClassName:
	Statement1
	...
	Statement n

class derived1(base):
	Statement1
	...
	Statement n

class derived2(derived1):
	Statement1
	...
	Statement n
If a method is called on an instance of the derived class, it first tries to find it in the same class and if it is not available, it travels one step up and so on and so forth until it finds the method. This search can travel upto the parent / base class which is the topmost in the hierarchy.

A class in the middle of the hierarchy can also have Multiple Inheritance as shown below:.



Let us understand using an example:
Person is the base class
Student is derived from Person
Address is derived from Student
So when we create an instance of Address, we can access all the methods of Student and Person.

Please click on the 
 button to understand more on multi-level-inheritance.


Observe the partial code given in the editor.
The Person class has methods setname() and getname() to set and get a person's name.
The Student class inherits from Person and adds methods setage() and getage() to set and get a student's age.
The Address class inherits from Student and adds methods setaddress() and getaddress() to set and get a student's address.
Your task is to write Python code that creates an instance of the Address class, takes input for a person's name, age, and address, and then uses the appropriate methods to set and get these attributes. Make sure to call the getname(), getage(), and getaddress() methods to print out the information after setting it.
