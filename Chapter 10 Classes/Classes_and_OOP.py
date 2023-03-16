import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        try:
            last_blank = name.rindex(' ')
            self.last_name = name[last_blank + 1:]
        except:
            self.last_name = name
        self.birthday = None

    def get_name(self):
        """Return self's full name"""
        return self.name

    def get_last_name(self):
        "Return self's last name"
        return self.last_name

    def set_birthday(self, birthday):
        "Assumes birthday is a type of datetime.date"
        self.birthday = birthday

    def get_age(self):
        "Return self's current age in years"
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).year

    def __lt__(self, other):
        """ Assumes other a person.
        Return true if self precedes other in alphabetical order and False otherwise. Comparison
        is based on last names but if these are the same full names are compared"""
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __str__(self):
        """Return self's name"""
        return self.name


class MIT_person(Person):
    next_id_num = 0  # MIT Identification Number

    def __init__(self, name):
        super().__init__(name)
        self.id_num = MIT_person.next_id_num
        MIT_person.next_id_num += 1
    def get_id_num(self):
        return self.id_num

    def __lt__(self, other):
        return self.id_num<other.id_num

class Student(MIT_person):
    pass
class UG(Student):

    def __init__(self,name,class_year):
        super().__init__(name)
        self.year=class_year

    def get_class(self):
        return self.year
class Grad(Student):
    pass

class Grades(object):
    def __init__(self):
        """Create empty grade book"""
        self.students=[]
        self.grades={}
        self.is_sorted=True

    def add_student(self,student):
        """Assumes Student is of type Student class
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.get_id_num()]=[]
        self.is_sorted=False

    def add_grade(self,student,grade):
        """Assummes grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in Mapping')
    def get_grades(self,student):
        """Return list of grades for student"""
        try:
            return self.grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in Mapping')
    def get_students(self):
        """Return a sorted list of students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted=True
        return self.students[:]
    def __str__(self):
        if self.students==[]:
            return ()
        else:
            print(self.students)

def grade_report(course):
    """Assumes course is of Grade class type created above"""
    report=''
    for s in course.get_students():
        tot=0.0
        num_grades=0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot / num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
        return report



