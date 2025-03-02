import unittest
from lib.enrollment import Student, Course, Enrollment

class TestAggregateMethods(unittest.TestCase):
    def setUp(self):
        self.student = Student("John Doe")
        self.course1 = Course("Math 101")
        self.course2 = Course("History 201")
        self.student.enroll(self.course1)
        self.student.enroll(self.course2)
        self.student._grades = {self.course1: 85, self.course2: 90}

    def test_course_count(self):
        self.assertEqual(self.student.course_count(), 2)

    def test_aggregate_average_grade(self):
        self.assertEqual(self.student.aggregate_average_grade(), 87.5)

    def test_aggregate_enrollments_per_day(self):
        Enrollment(self.student, self.course1)
        Enrollment(self.student, self.course2)
        enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
        self.assertEqual(len(enrollments_per_day), 1)  # Assuming both enrollments are on the same day

if __name__ == "__main__":
    unittest.main()
