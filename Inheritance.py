class Person:
  def setname(self,name):
    self.name=name
  def getname(self):
    print(self.name)
class Student(Person):
  def setage(self,age):
    self.age=age
  def getage(self):
    print(self.age)
class Address(Student):
  def setaddress(self,address):
    self.address=address
  def getaddress(self):
    print(self.address)
s1=Address()
Name=input()
Age=int(input())
Place=input()
s1.setaddress(Place)
s1.setage(Age)
s1.setname(Name)

s1.getname()
s1.getage()
s1.getaddress()
