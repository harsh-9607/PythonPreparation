class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

class course:
    def __init__(self,max_students,course_name):
        self.course_name= course_name
        self.max_students = max_students
        self.students = []
        print(f"Course name {self.course_name}")

    def add_students(self,student):
        if len(self.students)==self.max_students:
            print(f"You already have {self.max_students} students in this course")
            return False
        else:
            self.students.append(student)

    def student_profiles(self):
        print([[std.name, std.grade] for std in self.students])

    def avg_grade(self):
        total = sum([std.grade for std in self.students])
        print(total/self.max_students)

s1 = student("Harsh",99)
s2 = student("Sara",100)

c1= course(2,"Lovey lovey")

c1.add_students(s1)
c1.add_students(s2)
c1.add_students(student("Gatita",99))
c1.student_profiles()

print(c1.avg_grade())      



