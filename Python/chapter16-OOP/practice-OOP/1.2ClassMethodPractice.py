class Grade_system:
    student_pass= 0
    student_fail = 0 

    topper = None

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        if self.gpa>=3:
            Grade_system.student_pass+=1
        else:
            Grade_system.student_fail+=1

        #update_topper

        if Grade_system.topper is None:
            Grade_system.topper = self
        elif self.gpa >Grade_system.topper.gpa:
            Grade_system.topper = self


    def __str__(self):
        return f"{self.name} - {self.gpa} - {self.get_grade()}"


    def get_grade(self):
        if self.gpa>=3:
            Pass_message = "Pass"
        else:
            fail_message = "Fail"


    @classmethod
    def pass_fail(cls):
        return f"Pass: {cls.student_pass}\nFail: {cls.student_fail}"

    @classmethod
    def get_topper(cls):
        if cls.topper:
            return f"Topper: {cls.topper.name} with GPA {cls.topper.gpa}"
    
    def get_grade(self):
        if self.gpa>=3:
            
            return "Pass"
        else:
            
            return "Fail"
        
    



student1 = Grade_system("Bulbul", 5.5)
student2 = Grade_system("ZiPPO", 2)
student3 = Grade_system("Alkama", 5.7)


# print(f"{student1.name} - {student1.gpa} - {student1.get_grade()}")

print(student1)
print(student2)
print(student3)

print(Grade_system.pass_fail())

print(Grade_system.get_topper())