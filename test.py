import random

students = []

for i in range(20):
    students.append({"student": str(i)})

print(students)

students2 = [({"student": str(i)}) for i in range(20)]

print(students2)