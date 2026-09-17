import multiprocessing
import time


def calculate_average(scores: list) -> float:
    """Calculate and return the average of a list of scores."""
    return sum(scores) / len(scores)


def process_student(name: str, scores: list, result_queue: multiprocessing.Queue) -> None:
    """Process a single student's scores in a separate process."""
    time.sleep(1)  # simulate a heavy computation
    average = calculate_average(scores)
    result_queue.put((name, average))


def main() -> None:
    students = {
        "Jane Smith": [88, 92, 79],
        "John Doe": [60, 55, 70],
        "Mary Jones": [95, 98, 90],
    }

    result_queue = multiprocessing.Queue()
    processes = []
    start_time = time.time()

    for name, scores in students.items():
        process = multiprocessing.Process(
            target=process_student, args=(name, scores, result_queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    print("Results:")
    while not result_queue.empty():
        name, average = result_queue.get()
        print(f"{name}: {average:.2f}")

    print(f"\nProcessed {len(students)} students in {end_time - start_time:.2f} seconds (parallel)")


if __name__ == "__main__":
    main()