__all__ = ['Student']

from functools import reduce

class Student(object):
    def __init__(self, id, firstName, lastName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.setCourses(courses)

    def setCourses(self, courses: dict) -> None:
        if courses == None:
            self.courses = dict()
        else:
            self.courses = courses

    def gpa(self) -> float:
        if not self.courses:
            return 0
        gpa_sum = reduce(lambda a, b: a + b, self.courses.values())
        return gpa_sum / len(self.courses)

    def addCourse(self, course: str, score: float) -> None:
        assert self.isNumeric(score), "Score needs to be an int or float between 0 and 4"
        assert self.isValidScore(score), "Score should be between 0 and 4"
        self.courses[course] = score

    def addCourses(self, courses) -> None:
        assert isinstance(courses, dict), "Please enter courses in a dictionary {}"
        self.courses.update(courses)

    def __str__(self) -> str:
        return f'{self.id: <9} {self.lastName: <19} {self.firstName: <14} {self.gpa(): >8.3f}  {", ".join(self.courses.keys()): >10}'

    def __repr__(self) -> str:
        return f'{self.id},{self.lastName},{self.firstName},{self.courses.keys()}'
    
    @staticmethod
    def header():
        print(f"{'ID': <10}{'Last Name': <20}{'First Name': <20}{'GPA': <5}{'Courses': <30}")
        print(f"{'=' * 98}")
        return

    @staticmethod
    def isNumeric(input):
        return isinstance(input, (int, float))
    
    @staticmethod
    def isValidScore(value):
        return 0 <= value <= 4
    
if __name__ == '__main__':
    def printStudents(s: list[Student]) -> None:
        Student.header()
        for student in s:
            print(str(student))
        print("\n")

    def getEnrolledStudents(students: list[Student], course: str) -> list[Student]:
        enrolledStudents = [s for s in students if course in s.courses.keys()]
        assert enrolledStudents, f"No one is enrolled in {course}"
        return enrolledStudents
    
    def getHonorRoll(students: list[Student], value: float) -> list[Student]:
        honorRollStudents = [s for s in students if s.gpa() >= value]
        assert honorRollStudents, f"No one has a GPA >= {value}"
        return honorRollStudents

    students = [Student(123456, 'Johnnie', 'Smith'),
                Student(234567, 'Jamie', 'Strauss', ),
                Student(345678, 'Jack', 'O\'Neill'),
                Student(456789, 'Susie', 'Marks' ),
                Student(567890, 'Frank', 'Marks'),
                Student(654321, 'Annie', 'Marks', {'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00 }),
                Student(456789, 'John', 'Smith'),
                Student(987456, 'Judy', 'Smith', {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00 }),
                Student(111354, 'Kelly', 'Williams', {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50 }),
                Student(995511, 'Brad', 'Williams', {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00 })
                ]
    
    students[0].addCourse('CSE-101', 3.50)
    students[0].addCourse('CSE-102', 3.00)
    students[0].addCourse('CSE-201', 4.00)
    students[0].addCourse('CSE-220', 3.75)
    students[0].addCourse('CSE-325', 4.00)
    students[2].addCourse('CSE-101', 2.50)
    students[2].addCourse('CSE-102', 3.50)
    students[2].addCourse('CSE-103', 3.00)
    students[2].addCourse('CSE-104', 4.00)
    students[6].addCourse('CSE-101', 2.50)
    students[6].addCourse('CSE-103', 3.00)
    students[6].addCourse('CSE-210', 3.50)
    students[6].addCourse('CSE-260', 4.00)
    students[1].addCourses({'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00 })
    students[3].addCourses({'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00 })
    students[4].addCourses({'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00 })
    
    printStudents(students)    

    # Query 1
    lastNameAscending: list[Student] = sorted(students, key=lambda student: (student.lastName, student.firstName), reverse=True)
    print("QUERY 1: Students sorted by lastName, FirstName in ascending order")
    printStudents(lastNameAscending)

    # Query 2
    gpaDescending: list[Student] = sorted(students, key=lambda student: student.gpa(), reverse=True)
    print("QUERY 2: Students with GPA in Descending Order")
    printStudents(gpaDescending)

    # Query 3
    uniqueCourses = set(element for s in students for element in s.courses.keys())
    print("QUERY 3: Course List")
    print(f"Count: {len(uniqueCourses)}, {sorted(uniqueCourses)}\n")

    # Query 4
    enrolledStudents: list[Student] = getEnrolledStudents(students, 'CSE-201')
    print("QUERY 4: Students in CSE-201")
    printStudents(enrolledStudents)

    # Query 5
    honorRollGpa: float = 3.5
    honorRoll: list[Student] = getHonorRoll(students, honorRollGpa)
    print("QUERY 5: Students with GPA >= 3.5")
    printStudents(honorRoll)
    

    

    