# Get the student's score
score = int(input("Enter student's score: "))

# Determine the result using conditional statements
if score >= 90:
    grade = "A"
    remark = "Excellent"
elif score >= 80:
    grade = "B"
    remark = "Very Good"
elif score >= 70:
    grade = "C"
    remark = "Good"
elif score >= 60:
    grade = "D"
    remark = "Fair"
else:
    grade = "F"
    remark = "Fail"

# Display the result
print("\n--- Result ---")
print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")