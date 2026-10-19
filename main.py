"""Run the Student and Course lab tasks."""

from course import Course, InvalidMarksError, load_course


class Student:
    """Represent a student and show whether they passed."""

    def __init__(self, name, marks):
        """Store the student's name and marks."""
        self.name = name
        self.marks = marks

    def passed(self):
        """Return True when the student's marks are at least 50."""
        return self.marks >= 50

    def __str__(self):
        """Return the student's name, marks, and pass/fail status."""
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"


# Task 1: Student class
students = [
    Student("Ali", 72),
    Student("Sara", 45),
    Student("Omar", 50),
]

for student in students:
    print(student)

print()

# Tasks 2 and 3: Course methods and custom exception
course = Course("Programming for AI")
course.add_student("Ali", 88)
course.add_student("Sara", 92)
course.add_student("Omar", 75)

print(len(course))
print(course.average())
print(course.top_student())

try:
    course.add_student("Bilal", 120)
except InvalidMarksError as error:
    print("Error:", error)

print(course)
print()

# Task 4: Load marks from the file
loaded_course = load_course("Programming for AI", "marks.txt")
print(loaded_course)
print("Top student:", loaded_course.top_student())

# Uncomment this line to test the missing-file message:
# load_course("Programming for AI", "mark.txt")
