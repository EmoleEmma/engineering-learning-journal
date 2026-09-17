import asyncio
import time


async def fetch_student_scores(name: str, delay: float) -> tuple:
    """Simulate fetching a student's scores from a slow source (e.g. a database or API)."""
    print(f"Fetching scores for {name}...")
    await asyncio.sleep(delay)
    print(f"Finished fetching {name}")
    return name, [88, 92, 79]


async def calculate_average_async(scores: list) -> float:
    """Calculate average (async for consistency, though this part is instant)."""
    return sum(scores) / len(scores)


async def process_student(name: str, delay: float) -> None:
    """Fetch a student's scores and calculate their average, asynchronously."""
    name, scores = await fetch_student_scores(name, delay)
    average = await calculate_average_async(scores)
    print(f"{name}'s average: {average:.2f}")


async def main() -> None:
    students = {
        "Jane Smith": 1.0,
        "John Doe": 1.5,
        "Mary Jones": 0.5,
    }

    start_time = time.time()

    # Run all student processing concurrently
    tasks = [process_student(name, delay) for name, delay in students.items()]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"\nAll students processed in {end_time - start_time:.2f} seconds (concurrently)")


if __name__ == "__main__":
    asyncio.run(main())