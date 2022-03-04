# First Program

def reverseString(hello):
    return hello[::-1]

name = input("Enter the Name")
reverse = reverseString(name)
print(reverse)


# Second Program
lst = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in lst:
    sum += i

print(sum)


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