from abc import ABC, abstractstaticmethod

class IPerson(ABC):
    
    @abstractstaticmethod  
    def print_data():
        "Implement in child class"
        
class PersonSigleton(IPerson):
    
    __instance = None
    
    @staticmethod
    def get_instance():
        if PersonSigleton.__instnace == None:
            PersonSigleton("Default Name", 0)
        return __instance
    
    def __init__(self, name, age):
        if PersonSigleton.__instance != None:
            raise Exception("Singleton was already instantiated.")
        else:
            self.name = name
            self.age = age
        
            PersonSigleton.__instance = self
    @staticmethod
    def print_data():
        print(f"{PersonSigleton.__instance}")
PersonSigleton.print_data()
p = PersonSigleton("Jhon",21)
PersonSigleton.print_data()
p1 = PersonSigleton("El",21)