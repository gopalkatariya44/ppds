# First Program

def reverseString(hello):
    return hello[::-1]

name = input("Enter the Name : ")
reverse = reverseString(name)
print(reverse)


# Second Program
lst = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in range(len(lst)):
    sum = lst[i]*2
    lst[i] = sum
print(lst)


# Third Program
student_a = "gopal"
student_b = "parth"
print("student_a = ",end="")
print(student_a)
print("student_b = ",end="")
print(student_b)
student_a,student_b = student_b,student_a
print("student_a = ",end="")
print(student_a)
print("student_b = ",end="")
print(student_b)

# 7 march code
# Types of Constructor
    # 1. Default Constructor
    # 2. Parameter Constructor
# Constructor is automatically call class object is created 
# Class member function name is always smaller case

import email


class Employee:
    increment_value = 1.05 # class Member variable

    # Constructor
    def __init__(self,first,last,payment):
        self.first = first
        self.last = last
        self.payment = payment
        # self.email = first+last+"@gmail.com"
        self.email = f"{first,last}@gmail.com"

    def name(name):   # 
        print(name)
    
# object
# Object is a refrence of class 
# Object use for access the class member variable and  memeber function 

employee = Employee("Parth","Ramanuj","This is a Payment")
employee = Employee("Gopal ","Katariya","$23")
print(employee.first)
print(employee.last)
print(employee.payment)
print(employee.email)

# in python encapsulation and polymorphism not achived 100%
# we can't achive access modifier not supported
# Method overriding supported but overloading is not supported
