class Student:
    def __init__(self,name,Class,university):
        self.name=name
        self.Class=Class
        self.university=university

    def introduce(self):
        print('Hello! My name is',self.name)
        
    def reply(self):
        print('Hello! Nice to meet you! I am',self.name)

class Master_student(Student):
    def __init__(self,name, Class, university, Master_program):
        super().__init__(name,Class, university)
        self.Master_program = Master_program
    
    def introduce(self):
        super().introduce()
    
    def reply(self):
        super().reply()


Student1=Master_student('Joana','Advanced Programmingm','UCG', 'Masters P1')
Student2=Master_student('Sofia','Imunology','AUC', 'Master P2')

Student1.introduce()
Student2.reply()