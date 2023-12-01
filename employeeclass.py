"""
Create a class Employee having data members as name, designation and basic.
Create a constructor to initalize data in the data members.
Override the str() function to return the data in following format
  "Name is {name},Designation is {designation} and Basic is {basic}"
Create a function salary() that returns salary of the employee based on following  rules
  Salary is 1.5 times of basic if basic>=50000
  Salry is 2 times of basic is basic is >=30000
  Salary is 3 times of basic if basi is >=10000
  Salary is 4 times of basic for others

Create an object of Employee class having data taken from user in following format
  name, designation, basic
Show the output in following format
  Salary of {name} is {salary}
Example
  Input: Rohit, Manager, 5000
  Output: Salary of Ritesh is 20000
"""

class Employee:
  def __init__(self,name,designation,basic):
    self.name=name
    self.designation=designation
    self.basic=basic
  def salary(self):
    if self.basic>=50000:
      s=self.basic*1.5
    elif self.basic>=30000:
      s=self.basic*2
    elif self.basic>=10000:
      s=self.basic*3
    else:
      s=self.basic*4
    return s
  def __str__(self):
    return f"Name is {self.name},Designation is {self.designation} and Basic is {self.basic}";

# Data Input
name,designation,basic=input().split(',')
basic=int(basic)

# Creating Object
e=Employee(name,designation,basic)

# Calling function
salary=e.salary()

# Print the output
print(f"Salary of {name} is {salary}")
