"""Course management classes and file loading functions."""


class InvalidMarksError(Exception):
    """Raised when a student's marks are outside the valid range."""


class Course:
    """Store student marks for a course and provide summary methods."""

    def __init__(self, name):
        """Initialize a course with its name and an empty marks dictionary."""
        self.name = name
        self.marks = {}

    def add_student(self, student: str, marks: int) -> None:
        """Add a student's marks after checking that they are between 0 and 100."""
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self):
        """Return the average of all marks in the course."""
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        """Return the name of the student with the highest marks."""
        return max(self.marks, key=self.marks.get)

    def __len__(self):
        """Return the number of students in the course."""
        return len(self.marks)

    def __str__(self):
        """Return a readable summary of the course."""
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"


def load_course(name: str, filename: str) -> Course:
    """Load valid student marks from a text file and skip invalid lines."""
    course = Course(name)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    student, mark = line.split(",")
                    marks = int(mark)
                    course.add_student(student, marks)
                except ValueError:
                    student_name = line.split(",", 1)[0]
                    print(f"Skipping {student_name}: marks is not a number")
                except InvalidMarksError as error:
                    print(f"Skipping: {error}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)
