import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        durations = [3, 5, 1, 2]
        results = executor.map(func, durations)
        for result in results:
            print(f"Finished sleeping for {result} seconds")

poolingDemo()
