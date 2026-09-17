def factorial(n: int) -> int:
    """Recursive function to calculate factorial (used here as a generic recursion example)."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_scores_recursive(scores: list) -> float:
    """Recursively sum a list of scores."""
    if not scores:
        return 0
    return scores[0] + sum_scores_recursive(scores[1:])


def main():
    # Data structures: dict of students with list of scores
    students = {
        "Jane Smith": [88, 92, 79],
        "John Doe": [60, 55, 70],
        "Mary Jones": [95, 98, 90],
    }

    # List comprehension: calculate averages for all students
    averages = {name: sum(scores) / len(scores) for name, scores in students.items()}
    print("Averages (via dict comprehension):", averages)

    # List comprehension: filter students who passed (average >= 60)
    passing_students = [name for name, avg in averages.items() if avg >= 60]
    print("Passing students:", passing_students)

    # Sorting: rank students by average, highest first
    ranked = sorted(averages.items(), key=lambda item: item[1], reverse=True)
    print("\nRanked students:")
    for rank, (name, avg) in enumerate(ranked, start=1):
        print(f"{rank}. {name}: {avg:.2f}")

    # Recursion example 1: factorial
    print(f"\nFactorial of 5: {factorial(5)}")

    # Recursion example 2: recursive sum of a student's scores
    jane_scores = students["Jane Smith"]
    print(f"Recursive sum of Jane's scores: {sum_scores_recursive(jane_scores)}")


if __name__ == "__main__":
    main()