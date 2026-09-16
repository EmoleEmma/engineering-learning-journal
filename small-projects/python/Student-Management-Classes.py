class Student:
    """Represents a student with name, scores, and result info."""

    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def calculate_average(self):
        """Calculate and return the average of the three scores."""
        total = self.score1 + self.score2 + self.score3
        average = total / 3
        return average

    def determine_result(self):
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

    def display_result(self):
        """Display this student's full result."""
        average = self.calculate_average()
        grade, remark = self.determine_result()
        print("\n--- Student Result ---")
        print(f"Name: {self.name}")
        print(f"Average Score: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Remark: {remark}")


def main():
    students = []

    num_students = int(input("How many students do you want to enter? "))

    for i in range(num_students):
        print(f"\nEnter details for student {i + 1}:")
        name = input("Name: ")
        score1 = float(input("Score 1: "))
        score2 = float(input("Score 2: "))
        score3 = float(input("Score 3: "))

        student = Student(name, score1, score2, score3)
        students.append(student)

    # Display all student results
    for student in students:
        student.display_result()


# Run the program
main()