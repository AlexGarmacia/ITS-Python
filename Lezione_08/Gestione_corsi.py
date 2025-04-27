class Room:
    def __init__(self, room_id: int, floor: int, seats: int):
        self.room_id: int = room_id          
        self.floor: int = floor            
        self.seats: int = seats              
        self.area: int = self.seats * 2      

    def get_id(self) -> int:
        return self.room_id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    def get_area(self) -> int:
        return self.area

    
class Room:
    def __init__(self, room_id: int, floor: int, seats: int):
        self.room_id: int = room_id          
        self.floor: int = floor              
        self.seats: int = seats              
        self.area: int = self.seats * 2  

    def get_id(self) -> int:
        return self.room_id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    def get_area(self) -> int:
        return self.area

class Person:
    def __init__(self, name:str, surname:str, age:int, cf:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.cf = cf
    def set_group(self, group:str):
        self.group = group

class Student(Person):
    pass

class Lecturer(Person):
    pass


class Group:
    def __init__(self, name:str, limit:int, students:list[Person], lecturers:list[Person]):
        self.name = name
        self.limit = limit
        self.students = students
        self.lecturers = lecturers
    
    def get_name(self) -> str:
        return self.name
    def get_limit(self) -> int:
        return self.limit
    def add_student(self, student: 'Student'):
        return self.students
    def get_lecturers(self) -> int:
        return max(1, len(self.students) // 10)
    
    def add_student(self, student: Student):
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self.name)   
        else:
            print(f"Non puoi aggiungere altri studenti: limite raggiunto ({self.limit})")

    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
        else:
            print(f"Non puoi aggiungere altri docenti: limite di {self.get_limit_lecturers()} docenti raggiunto.")
    
class Course:
    def __init__(self, name: str):
        self.name: str = name               # Nome del corso
        self.groups: list[Group] = []        # Lista dei gruppi

    def register(self, student: Student):
        # Cerca il primo gruppo disponibile con posti per lo studente
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                print(f"{student.name} {student.surname} registrato nel gruppo {group.get_name()}.")
                return
        print(f"Impossibile registrare {student.name} {student.surname}: nessun gruppo disponibile.")

    def get_groups(self) -> list:
        return self.groups

    def add_group(self, group: Group):
        self.groups.append(group)
        print(f"Gruppo {group.get_name()} aggiunto al corso {self.name}.")

    
        
