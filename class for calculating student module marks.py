# program to calculate overall module mark and grade

# defines class 'Student'
class Student:
    '''stores names and exam data'''

    # constructor method for instantiating objects
    # variables 'name', 'cwork', and 'exam' initialised
    def __init__(self, name, exam, cwork):
        self.name = name
        self.exam = exam
        self.cwork = cwork

    # calculates exam percentage
    def exam_percent(self):
        total_exam_mark = 90
        exam_percentage = (self.exam / total_exam_mark) * 100
        return round(exam_percentage)

    # calculates coursework percentage
    def cwork_percent(self):
        total_cwork_mark = 90
        cwork_percentage = (self.cwork / total_cwork_mark) * 100
        return round(cwork_percentage)

    # calculates module percentage
    def module_percent(self):
        total_mod_mark = 180
        mod_percentage = ((self.cwork + self.exam) / total_mod_mark) * 100
        return round(mod_percentage)

    # calculates overall grade for module
    def overall_grade(self, module_percent, cwork_percent, exam_percent):
        if module_percent >= 40:
            if cwork_percent >= 30 and exam_percent >= 30:
                return 'Pass'
            else:
                return 'Fail(Threshold)'
        else:
            return 'Fail'
            
    
# calling constructor to create objects of the class
student1 = Student('Bob', 50, 75)
student2 = Student('Alice', 60, 45)
student3 = Student('Molly', 20, 20)
student4 = Student('Fred', 75, 20)
student5 = Student('George', 10, 70)

#calling methods on objects
print (student1.module_percent())
print (student1.exam_percent())
print (student1.cwork_percent())
   
# calling multiple methods on objects
print (student1.overall_grade(student1.module_percent(), student1.cwork_percent(), student1.exam_percent()))
print (student3.overall_grade(student3.module_percent(), student3.cwork_percent(), student3.exam_percent()))
print (student5.overall_grade(student5.module_percent(), student5.cwork_percent(), student5.exam_percent()))



