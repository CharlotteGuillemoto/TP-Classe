from collections import defaultdict

class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.matière={}
        

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    


    def add_grade(self, topic: str, grade: float) -> None:
            if not ( 0 <= grade <= 20):
                 raise ValueError("Grade must be between 0 and 20")
            self.topic=topic
            self.grade=grade
            if self.topic in self.matière.keys():
                self.matière[self.topic].append(self.grade)
            else :
                self.matière[self.topic]=[self.grade]

    def followed_topics(self):
         return(list(self.matière.keys()))
            
    
    def compute_average(self, course: str) -> float:
        if course not in self.grades or len(self.grades[course]) == 0:
            raise ValueError(f"No grades recorded for course: {course}")
        return sum(self.grades[course]) / len(self.grades[course])
    
    def report(self):
        """ génère un rapport formaté des moyennes par matière """
        report_lines = []
        header = f"Report for student {self.first_name} {self.last_name}"
        report_lines.append(header)
        report_lines.append("+===============+===============+")
        report_lines.append("|     Topic     |    Average    |")
        report_lines.append("+===============+===============+")
        
        for topic in self.followed_topics():
            average = self.compute_average(topic)
            report_lines.append(f"|  {topic:<13}|    {average:>6.2f}     |") # Format topic left-aligned in 13 spaces, average right-aligned in 6 spaces with 2 decimals
            report_lines.append("+---------------+---------------+")
        
        return "\n".join(report_lines)


try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#print(student.followed_topics)