class person:
    nop=0
    
    def __init__(self,name):
        self.name = name
        person.add_people()
        print(f"number of people {person.nop}")

    @classmethod    
    def number_of_people(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

p1= person("me")
person.number_of_people()