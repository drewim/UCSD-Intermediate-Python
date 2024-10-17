from Student import *
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(123456, "John", "Doe")
        self.courses = {'CSE-101': 3.5, 'MATH-220': 3.0}

    
    def test_init(self):
        self.assertEqual(self.student.id, 123456)
        self.assertEqual(self.student.firstName, 'John')
        self.assertEqual(self.student.lastName, 'Doe')
        self.assertEqual(self.student.courses, {})

    def test_setCourses(self):
        self.student.setCourses(self.courses)
        self.assertEqual(self.student.courses, self.courses)

    def test_gpa(self):
        self.assertEqual(self.student.gpa(), 0)
        self.student.courses = self.courses
        self.assertAlmostEqual(self.student.gpa(), 3.25)    

    def test_addCourse(self):
        self.student.addCourse("English", 3.0)
        self.assertDictEqual(self.student.courses, {"English": 3.0})

    def test_addCourses(self):
        self.student.addCourses(self.courses)
        self.assertDictEqual(self.student.courses, self.courses)

    def test_str(self):
        self.student.courses = self.courses
        expected = "123456    Doe                 John              3.250  CSE-101, MATH-220"
        self.assertEqual(str(self.student), expected)

    def test_repr(self):
        self.student.courses = {"Math": 3.5, "Science": 4.0}
        expected = "123456,Doe,John,dict_keys(['Math', 'Science'])"
        self.assertEqual(repr(self.student), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_header(self, mock_stdout):
        Student.header()
        expected_output = "ID        Last Name           First Name          GPA  Courses                       \n==================================================================================================\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_isNumeric(self):
        self.assertTrue(Student.isNumeric(4))
        self.assertTrue(Student.isNumeric(2.3))
        self.assertFalse(Student.isNumeric("4"))

    def test_isValidScore(self):
        self.assertTrue(Student.isValidScore(0))
        self.assertTrue(Student.isValidScore(2.1))
        self.assertTrue(Student.isValidScore(4))
        self.assertFalse(Student.isValidScore(-1))
        self.assertFalse(Student.isValidScore(4.1))

class TestStudentQueries(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student(123456, 'Johnnie', 'Smith', {'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}),
            Student(234567, 'Jamie', 'Strauss', {'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00}),
            Student(345678, 'Jack', 'O\'Neill', {'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00}),
            Student(456789, 'Susie', 'Marks', {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00}),
            Student(567890, 'Frank', 'Marks', {'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00})
        ]
    
    def test_last_name_first_nameascending_sort(self):
        sorted_students = sorted(self.students, key=lambda student: (student.lastName, student.firstName))
        self.assertEqual(sorted_students[0].lastName, 'Marks')
        self.assertEqual(sorted_students[0].firstName, 'Frank')
        self.assertEqual(sorted_students[-1].lastName, 'Strauss')

    def test_gpa_descending_sort(self):
        sorted_students = sorted(self.students, key=lambda student: student.gpa(), reverse=True)
        self.assertGreater(sorted_students[0].gpa(), sorted_students[1].gpa())

    def test_unique_courses(self):
        unique_courses = set(course for student in self.students for course in student.courses.keys())
        expected_courses = {'CSE-101', 'CSE-102', 'CSE-103', 'CSE-104', 'CSE-201', 'CSE-202', 'CSE-203', 'CSE-220', 'CSE-301', 'CSE-302', 'CSE-310', 'CSE-325', 'CSE-401'}
        self.assertEqual(unique_courses, expected_courses)
 
    def test_get_enrolled_students(self):
        def getEnrolledStudents(students, course):
            return [s for s in students if course in s.courses.keys()]

        enrolled_cse201 = getEnrolledStudents(self.students, 'CSE-201')
        self.assertEqual(len(enrolled_cse201), 2)
        self.assertIn(self.students[0], enrolled_cse201)
        self.assertIn(self.students[4], enrolled_cse201)

        enrolled_cse999 = getEnrolledStudents(self.students, 'CSE-999')
        self.assertEqual(len(enrolled_cse999), 0)

    def test_get_honor_roll(self):
        def getHonorRoll(students, value):
            return [s for s in students if s.gpa() >= value]

        honor_roll_3_5 = getHonorRoll(self.students, 3.5)
        self.assertEqual(len(honor_roll_3_5), 2)
        self.assertIn(self.students[0], honor_roll_3_5)
        self.assertIn(self.students[1], honor_roll_3_5)

        honor_roll_4_0 = getHonorRoll(self.students, 4.0)
        self.assertEqual(len(honor_roll_4_0), 0)
        
if __name__ == '__main__':
    unittest.main()