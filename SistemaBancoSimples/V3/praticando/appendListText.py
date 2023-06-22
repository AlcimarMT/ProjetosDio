class ObjectHistory:
    def __init__(self,text):
        self.text = text

    @classmethod
    def addHistory(cls,appendHistory):
        return cls(appendHistory)
        
class ObjectAge:
    def __init(self,age):
        self.age = age   
    
    @classmethod
    def ageChanger(cls,numberAge):
        return cls(numberAge)
    
class MyObject:
    def __init__(self,history,age):
        self.history = ObjectHistory(history)
        self.age = ObjectAge(age)

    @property
    def history(self):
        return self.history
    
    @property
    def age(self):
        return self.age
    
myObjct = MyObject("Nothing here",24)



