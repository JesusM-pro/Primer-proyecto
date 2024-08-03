class Wizzard:
    def __init__(self,name):
        if not name:
            raise ValueError ("missing name")
        self.name = name

class Student(Wizzard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizzard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

def __str__(self):
    return f'{self.name} name, {self.house} house, {self.subject}subject'



wizzard = Wizzard(input("Who is the Wizzard? "))
student = Student(input("Who is the student? "),'Griffindor')
professor = Professor (input("Who is the professor? "),"Defense against the dark arts")
print(wizzard)
print(student)
print(professor)