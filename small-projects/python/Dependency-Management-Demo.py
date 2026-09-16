from tabulate import tabulate


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

    # Build a table of results using tabulate
    table_data = []
    for student in students:
        average = student.calculate_average()
        grade, remark = student.determine_result()
        table_data.append([student.name, f"{average:.2f}", grade, remark])

    headers = ["Name", "Average", "Grade", "Remark"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))


# Run the program
main()