class Wizard:

    def __init__(self, name):
        self.name = name


class Student(Wizard):

    def __init__(self, name, house):
        super().__init__(name)
        self._house = house

    @classmethod
    def get(cls):
        name = input('Student Name: ')
        house = input('Student House: ')
        return cls(name, house)

    def __str__(self):
        return f'{self.name} {self.house}'

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        self._house = house


class Professor(Wizard):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    @classmethod
    def get(cls):
        name = input('Prof Name: ')
        subject = input('Prof Subject: ')
        return cls(name, subject)

    def __str__(self):
        return f'{self.name} {self.subject}'

def main():
    student = Student.get()
    prof = Professor.get()
    print(student)
    print(prof)
    student.house = 'Slitherin'
    print(student.house)

main()