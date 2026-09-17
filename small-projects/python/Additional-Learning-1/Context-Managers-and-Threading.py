import threading
import time


class StudentFileManager:
    """Custom context manager for handling a student report file."""

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening {self.filename}...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}...")
        self.file.close()


def process_student(name: str, delay: float):
    """Simulate processing a student's result (e.g., grading), used in a thread."""
    print(f"Processing {name}...")
    time.sleep(delay)
    print(f"Finished processing {name}")


def main():
    # Context manager example: writing to a file safely
    with StudentFileManager("thread_report.txt", "w") as file:
        file.write("Student Processing Report\n")
        file.write("=" * 30 + "\n")

    # Threading example: process multiple students concurrently
    students = ["Jane Smith", "John Doe", "Mary Jones"]

    threads = []
    start_time = time.time()

    for student in students:
        thread = threading.Thread(target=process_student, args=(student, 1))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\nAll students processed in {end_time - start_time:.2f} seconds (concurrently)")


if __name__ == "__main__":
    main()