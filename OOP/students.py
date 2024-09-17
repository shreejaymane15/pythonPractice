class Student:
    def  __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def  name(self):
        return self._name
    
    # Setter
    @name.setter
    def  name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

        
    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter    
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    # student = get_student()
    # print(f"{student.name} from {student.house}")
    print(Student.get())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()