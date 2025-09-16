class Student_Grade:

    topper = None
    pass_student = 0
    fail_student = 0

    Students = []

    def __init__(self, name, gpa, batch):
        self.name = name
        self.gpa = gpa
        self.batch = batch

        Student_Grade.Students.append(self)

        if self.gpa>=3:
            Student_Grade.pass_student+=1
        else:
            Student_Grade.fail_student+=1

        if Student_Grade.topper is None:
            Student_Grade.topper = self
        elif self.gpa>Student_Grade.topper.gpa :
            Student_Grade.topper = self

    def pass_or_fail(self):
        if self.gpa>=3:
            return "Pass"
        else:
            return "Fail"

    @classmethod
    def pass_fail(cls):
        return f"Pass: {cls.pass_student}\nFail: {cls.fail_student}"

    @classmethod
    def get_topper(cls):
        return f"Topper is {cls.topper.name} with GPA {cls.topper.gpa}"
    

    @classmethod
    def get_batch_average(cls, batch):
        batch_students = []

        for i in cls.Students:
            if i.batch == batch:
                batch_students.append(i.gpa)

        if batch_students:
            return f"Batch: {batch} - Average: {sum(batch_students)/len(batch_students)}"
            

        return f"No students in this batch"
    

 



student1 = Student_Grade('Bulbul', 3.5, 2025)
student2 = Student_Grade('Alkama', 5.5, 2024)
student3 = Student_Grade('Zippo', 2.5, 2025)


print(f"{student1.name} - {Student_Grade.pass_or_fail(student1)}")
print(f"{student2.name} - {Student_Grade.pass_or_fail(student2)}")
print(f"{student3.name} - {Student_Grade.pass_or_fail(student3)}")

print(Student_Grade.pass_fail())

print(Student_Grade.get_topper())


print(Student_Grade.get_batch_average(2024))