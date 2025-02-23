from faker import Faker

fake = Faker()
class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduce(self):
        return f"Hello, my name is {self.name}, my address: {self.address} "

student1 = Student(fake.name(), fake.address())
print(student1.introduce())

"""Эта библиотека используется для создания фэйков 
данных чтобы тестить или заполнять базу данных"""