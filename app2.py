from Student import Student
# first Student is file name and second Student is class name

student1 = Student(name="Kevin", age=22, major="Master", gpa=3.5, is_on_probation=True )
student2 = Student(name="Mark", age=25, major="Master", gpa=3.8, is_on_probation=False )

print(student1.name)
print(student2.name)
print(student1.is_on_probation)