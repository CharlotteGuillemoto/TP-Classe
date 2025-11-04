from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def add_grade(topic: str; grade: float)

try:
    student = Student("Achille", "Talon")
    if repr(student) != "Achille Talon":
        raise Exception("There is an issue in your __repr__ method.")
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')