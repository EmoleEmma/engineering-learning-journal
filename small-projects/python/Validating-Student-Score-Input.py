def get_valid_score(prompt):
    """Prompt the user for a score and validate it, handling invalid input."""
    while True:
        try:
            score = float(input(prompt))
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100.")
            return score
        except ValueError as e:
            if str(e) == "Score must be between 0 and 100.":
                print(f"Invalid input: {e} Please try again.")
            else:
                print("Invalid input: Please enter a valid number. Try again.")


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


def main():
    try:
        name = input("Enter student's name: ")
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        score1 = get_valid_score("Enter first score: ")
        score2 = get_valid_score("Enter second score: ")
        score3 = get_valid_score("Enter third score: ")

        average = calculate_average(score1, score2, score3)
        grade, remark = determine_result(average)

        print("\n--- Student Result ---")
        print(f"Name: {name}")
        print(f"Average Score: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Remark: {remark}")

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nProgram execution completed.")


# Run the program
main()