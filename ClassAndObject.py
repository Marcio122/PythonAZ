class Student():
    def __init__(self):
        self.name = 'Marcio'
        self.age = 23
        self.marks = 100
        
    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)
        
s1 = Student()

print(s1.name)
s1.talk()