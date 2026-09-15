def calculate_average(score1, score2, score3):
    """Calculate and return the average of three scores."""
    total = score1 + score2 + score3
    average = total / 3
    return average


def determine_result(average):
    """Determine grade and remark based on the average score."""
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


def display_result(name, average, grade, remark):
    """Display the student's final result."""
    print("\n--- Student Result ---")
    print(f"Name: {name}")
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")


def main():
    # Get student information
    name = input("Enter student's name: ")
    score1 = float(input("Enter first score: "))
    score2 = float(input("Enter second score: "))
    score3 = float(input("Enter third score: "))

    # Use functions to process the data
    average = calculate_average(score1, score2, score3)
    grade, remark = determine_result(average)
    display_result(name, average, grade, remark)


# Run the program
main()