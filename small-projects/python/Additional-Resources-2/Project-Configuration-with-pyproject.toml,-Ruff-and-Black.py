"""
student_formatter_demo.py
A small script intentionally written to be checked/fixed by Ruff and Black.
"""

from typing import List, Tuple


class Student:
    """Represents a student and their scores."""

    def __init__(self, name: str, scores: List[float]) -> None:
        self.name = name
        self.scores = scores

    def average(self) -> float:
        """Return the average score."""
        return sum(self.scores) / len(self.scores)

    def result(self) -> Tuple[str, str]:
        """Return grade and remark based on average."""
        avg = self.average()
        if avg >= 90:
            return "A", "Excellent"
        elif avg >= 80:
            return "B", "Very Good"
        elif avg >= 70:
            return "C", "Good"
        elif avg >= 60:
            return "D", "Fair"
        else:
            return "F", "Fail"


def main() -> None:
    students = [
        Student("Jane Smith", [88, 92, 79]),
        Student("John Doe", [60, 55, 70]),
        Student("Mary Jones", [95, 98, 90]),
    ]

    for student in students:
        grade, remark = student.result()
        print(f"{student.name}: {student.average():.2f} ({grade} - {remark})")


if __name__ == "__main__":
    main()