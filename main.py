# class Student:
#     amount_of_student = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_student += 1
#
#
# vasya = Student(height=200)
# print("Vasya created",vasya.amount_of_student)
# tanya = Student(height=165)
# print("Tanya created",tanya.amount_of_student)

class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}"


vasya = Student("Vasya", 20)

print(vasya.name, vasya.age, vasya.introduce())
