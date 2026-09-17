from typing import Tuple, List


class Student:
    """Represents a student with name, scores, and result info."""

    def __init__(self, name: str, score1: float, score2: float, score3: float) -> None:
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def calculate_average(self) -> float:
        """Calculate and return the average of the three scores."""
        total = self.score1 + self.score2 + self.score3
        average = total / 3
        return average

    def determine_result(self) -> Tuple[str, str]:
        """Determine grade and remark based on the average score."""
        average = self.calculate_average()
        if average >= 90:
            grade = "A"
            remark = "Excellent"
        elif average >= 80:
            grade = "B"
            remark = "Very Good"
        elif average >= 70:
            grade = "C"
            remark = "Good"
        elif average >= 60:
            grade = "D"
            remark = "Fair"
        else:
            grade = "F"
            remark = "Fail"
        return grade, remark

    def display_result(self) -> None:
        """Display this student's full result."""
        average = self.calculate_average()
        grade, remark = self.determine_result()
        print("\n--- Student Result ---")
        print(f"Name: {self.name}")
        print(f"Average Score: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Remark: {remark}")


def main() -> None:
    students: List[Student] = []

    num_students = int(input("How many students do you want to enter? "))

    for i in range(num_students):
        print(f"\nEnter details for student {i + 1}:")
        name = input("Name: ")
        score1 = float(input("Score 1: "))
        score2 = float(input("Score 2: "))
        score3 = float(input("Score 3: "))

        student = Student(name, score1, score2, score3)
        students.append(student)

    for student in students:
        student.display_result()


# ---------------------------
# Tests
# ---------------------------

def run_tests() -> None:
    """Run simple tests to verify Student class behavior."""

    # Test 1: calculate_average with known values
    s1 = Student("Test A", 90, 90, 90)
    assert s1.calculate_average() == 90, "Average calculation failed for equal scores"

    # Test 2: calculate_average with mixed values
    s2 = Student("Test B", 88, 92, 79)
    expected_avg = (88 + 92 + 79) / 3
    assert abs(s2.calculate_average() - expected_avg) < 0.001, "Average calculation failed for mixed scores"

    # Test 3: determine_result returns correct grade for 'A'
    s3 = Student("Test C", 95, 95, 95)
    grade, remark = s3.determine_result()
    assert grade == "A" and remark == "Excellent", "Grade A boundary failed"

    # Test 4: determine_result returns correct grade for 'F'
    s4 = Student("Test D", 40, 30, 20)
    grade, remark = s4.determine_result()
    assert grade == "F" and remark == "Fail", "Grade F boundary failed"

    # Test 5: boundary case exactly at 60 (should be 'D', not 'F')
    s5 = Student("Test E", 60, 60, 60)
    grade, remark = s5.determine_result()
    assert grade == "D" and remark == "Fair", "Boundary at 60 failed"

    # Test 6: boundary case exactly at 90 (should be 'A')
    s6 = Student("Test F", 90, 90, 90)
    grade, remark = s6.determine_result()
    assert grade == "A" and remark == "Excellent", "Boundary at 90 failed"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
    main()