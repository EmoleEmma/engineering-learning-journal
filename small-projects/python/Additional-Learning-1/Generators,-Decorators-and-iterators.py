import time
from functools import wraps


def timer_decorator(func):
    """Decorator that prints how long a function takes to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] took {end - start:.6f} seconds")
        return result
    return wrapper


def score_generator(scores: list):
    """Generator that yields scores one at a time."""
    for score in scores:
        yield score


class StudentIterator:
    """Custom iterator that goes through a list of student names."""

    def __init__(self, students: list):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


@timer_decorator
def calculate_total(scores: list) -> float:
    """Calculate total using the generator (decorated to measure time)."""
    total = 0
    for score in score_generator(scores):
        total += score
    return total


def main():
    scores = [88, 92, 79]

    # Generator usage
    total = calculate_total(scores)
    print(f"Total score: {total}")

    # Custom iterator usage
    student_names = ["Jane Smith", "John Doe", "Mary Jones"]
    print("\nIterating through students:")
    for student in StudentIterator(student_names):
        print(f"- {student}")


if __name__ == "__main__":
    main()