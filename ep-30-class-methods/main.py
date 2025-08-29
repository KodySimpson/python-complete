## Class Methods - Methods that operate on the class itself rather than an instance
class Student:
    # Class variable - shared by all instances
    school = "MIT"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # We have a new student, so we increment the student count
        # so that we can keep track of how many students are in the school
        Student.student_count += 1
        
    # Class method - operates on the class itself
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # This makes sense to be an instance method because 
    # it uses data from the instance (name and age)
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, School: {self.school}"
    