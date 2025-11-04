
from student import Student
class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.students = []
        

    def add_student(self, student: Student):
        self.students.append(student)
        

    def __len__(self):
        return len(self.students)

    def __repr__(self):
        return f"Class {self.classname} - {len(self)} student(s)"
    
    def get_student(self, first_name: str, last_name:str):
        if Student(first_name, last_name) not in self.students: 
            return None
        else : 
            return Student(first_name, last_name)

    


classe = Class("P20")
student = Student("Matthieu", "Mazière")
classe.add_student(student)
new_student = classe.get_student("Matthieu", "Mazière")
#print(repr(student))
#print(repr(new_student))
assert student == new_student
#new_student = classe.get_student("Jérôme", "Adnot")
#assert new_student is None



