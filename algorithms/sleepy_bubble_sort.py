import time

def sleepy_bubble_sort(arr, delay=0.5):
    """
    Bubble sort with a delay to make it intentionally slow.
    :param arr: list of numbers to sort
    :param delay: time (in seconds) to wait between swaps
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Swapped: {arr[j+1]} and {arr[j]} -> {arr}")
                time.sleep(delay)  # Intentional delay
    return arr

# Example usage
numbers = [5, 2, 4, 1, 3]
print("Original:", numbers)
sorted_numbers = sleepy_bubble_sort(numbers, delay=0.3)
print("Sorted:  ", sorted_numbers)
