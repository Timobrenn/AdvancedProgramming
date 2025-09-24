class Student:
    def __init__(self, university, age, course):
        self.university = university
        self.age = age
        self.course = course

    def student_information(self):
        print(f"University: {self.university}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

# Child class
class MasterStudent(Student):
    def __init__(self, university, age, course, master_degree):
        # Call the constructor of the Parent class
        super().__init__(university, age, course)
        self.master_degree = master_degree

    def student_information(self):
        super().student_information()
        print(f"Master Degree: {self.master_degree}")