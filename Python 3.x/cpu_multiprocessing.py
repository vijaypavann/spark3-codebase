import multiprocessing, time

def cpu_bound(number: int) -> int:
    name = multiprocessing.current_process().name
    print(f"{name}: running for {number}")
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + i for i in range(20)] 
    start_time = time.time()
    find_sums(numbers)       
    print(f"Duration {time.time() - start_time} seconds")