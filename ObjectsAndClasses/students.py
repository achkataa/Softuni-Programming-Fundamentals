class students():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def grade(self):
        return self.grade

class course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        self.students.append(student)

student1 = students("Gosho", 14, 5)
student2 = students("Pesho", 16, 6)
student3 = students("Tosho", 17, 4)

course = course("English", 3)
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
print(course.students[2].name)