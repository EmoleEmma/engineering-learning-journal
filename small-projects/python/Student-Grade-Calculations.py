# Student Information
name = "John Doe"
age = 20
course = "Computer Science"
grade1 = 85
grade2 = 90
grade3 = 78

# Basic calculations using arithmetic operators
total = grade1 + grade2 + grade3
average = total / 3
highest = max(grade1, grade2, grade3)
lowest = min(grade1, grade2, grade3)

# Determine pass/fail using a comparison operator
passing_grade = 60
status = "Pass" if average >= passing_grade else "Fail"

# Predict age next year using an operator
age_next_year = age + 1

# Display the results
print("--- Student Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")

print("\n--- Grades ---")
print(f"Grade 1: {grade1}")
print(f"Grade 2: {grade2}")
print(f"Grade 3: {grade3}")

print("\n--- Calculations ---")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print(f"Status: {status}")
print(f"Age Next Year: {age_next_year}")