class student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def get_name(self):
        full_name = f"{self.name} {self.age}"
        return full_name
    
my_student = student("18", "sedrah")
print(my_student.get_name())
