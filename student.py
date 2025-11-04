from collections import defaultdict

class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.matière={}
        

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    


    def add_grade(self, topic: str, grade: float) -> None:
            self.topic=topic
            self.grade=grade
            if not ( 0 <= self.grade <= 20):
                 raise ValueError("Grade must be between 0 and 20")
            if self.topic in self.matière.keys():
                self.matière[self.topic].append(self.grade)
            else :
                self.matière[self.topic]=[self.grade]

    def followed_topics(self):
         return(list(self.matière.keys()))
            
    
    def compute_average(self, course: str) -> float:
        if course not in self.matière or len(self.matière[course]) == 0:
            return -1
        return sum(self.matière[course]) / len(self.matière[course])
    
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
    reference_lines = ['Report for student Albert Einstein',
                       '+===============+===============+',
                       '|     Topic     |    Average    |',
                       '+===============+===============+',
                       '|  Mathematics  |     12.80     |',
                       '+---------------+---------------+',
                       '|  Scubadiving  |     12.50     |',
                       '+---------------+---------------+']

    student = Student("Albert", "Einstein")
    student.add_grade("Mathematics", 12.80)
    student.add_grade("Scubadiving", 12.50)
    report = student.report()
    report_lines = report.strip().split('\n')
    for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == linestudent, f"Ligne {i} : attendu = {lineref}// obtenu = {linestudent}"
except AssertionError as e:
    print("Les deux chaines sont différentes")
    print(e)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
#print(student.followed_topics)