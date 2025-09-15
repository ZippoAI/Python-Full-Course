class Student:
    student_count = 0

    total_gpa  = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.total_gpa += gpa
        Student.student_count +=1
    
    #Instance Method
    def get_info(self):
        return f"{self.name} -- {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"total number of student: {cls.student_count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.student_count != 0:
            return f"Total gpa of all Student: {cls.total_gpa}/{cls.student_count:.2f} = {cls.total_gpa/cls.student_count} \nand total student: {cls.student_count}"
    
student1 = Student("Bulbul", 2.5)
student2 = Student("Zippo", 5)
student3 = Student("Alkama", 5.4)

print(student1.get_info())

print(Student.get_count())

print(Student.get_average_gpa())

