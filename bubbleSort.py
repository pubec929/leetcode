from random import randint
import time

def bubbleSort(array: list):
    while True:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
        if not swaps:
            break
    return array

if __name__ == "__main__":
    size = 10000
    rand_array = [randint(0, 100) for _ in range(size)]
    start_timestamp = time.time()
    bubbleSort(rand_array)
    elapsed = time.time() - start_timestamp
    print(elapsed)