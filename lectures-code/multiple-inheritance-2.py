

class Person:
    def greet(self):
        print('I am a Person')

class Teacher(Person):
    def greet(self):
        print('I am a Teacher')

class Student(Person):
    def greet(self):
        print('I am a Student')

class TeachingAssistant(Student, Teacher):
    def greet(self):
        print('I am a Teaching Assistant')
        
x = TeachingAssistant()
x.greet()

print(TeachingAssistant.__mro__)
print(TeachingAssistant.mro())
print(x.__class__.__mro__) 
