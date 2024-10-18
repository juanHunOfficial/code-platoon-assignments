from person import Person

class Staff(Person):
    
    def __init__(self, name, age, role, id, password):
        super().__init__(name, age, role, id, password)