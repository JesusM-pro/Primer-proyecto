class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError ("Missing name")
        if house not in ["Gryffindor",'Hufflepuff','Raveclaw', 'Slytherin']:
            raise ValueError ("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    def charm (self):
            if self.patronus == "Stag" :
                return "Fatima"
            elif self.patronus == "Otter":
                return "Luz"
            elif self.patronus == "Jack Rusell terrier":
                    return "Guadalupe"
            else:
                return "/"
        

def main():
    student = get_student()
    print("Expecto Patronum!")
    print( student.charm())


def get_student():
     name = input ("Name: ")
     house = input ("House: ")

if __name__ == "__main__":
     –main()