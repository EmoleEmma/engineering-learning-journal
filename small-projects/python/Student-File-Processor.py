def create_sample_input(filename):
    """Create a sample students.txt file if it doesn't already exist."""
    sample_data = (
        "Jane Smith,88,92,79\n"
        "John Doe,60,55,70\n"
        "Mary Jones,95,98,90\n"
    )
    with open(filename, "w") as file:
        file.write(sample_data)
    print(f"Sample input file created: {filename}")


def read_student_data(filename):
    """Read student data from a file. Each line: name,score1,score2,score3"""
    students = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            name = parts[0]
            score1 = float(parts[1])
            score2 = float(parts[2])
            score3 = float(parts[3])
            students.append((name, score1, score2, score3))
    return students


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


def write_report(students_results, output_filename):
    """Write a formatted report of all student results to an output file."""
    with open(output_filename, "w") as file:
        file.write("STUDENT RESULT REPORT\n")
        file.write("=" * 40 + "\n\n")
        for name, average, grade, remark in students_results:
            file.write(f"Name: {name}\n")
            file.write(f"Average Score: {average:.2f}\n")
            file.write(f"Grade: {grade}\n")
            file.write(f"Remark: {remark}\n")
            file.write("-" * 40 + "\n")


def main():
    input_filename = "students.txt"
    output_filename = "report.txt"

    try:
        # Read data from the input file
        students = read_student_data(input_filename)
    except FileNotFoundError:
        print(f"'{input_filename}' not found. Creating a sample file...")
        create_sample_input(input_filename)
        students = read_student_data(input_filename)

    # Process each student's data
    students_results = []
    for name, score1, score2, score3 in students:
        average = calculate_average(score1, score2, score3)
        grade, remark = determine_result(average)
        students_results.append((name, average, grade, remark))

    # Write the processed data to the output file
    write_report(students_results, output_filename)

    print(f"Report generated successfully: {output_filename}")


# Run the program
main()