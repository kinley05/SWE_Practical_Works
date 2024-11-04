import matplotlib.pyplot as plt
import numpy as np
import random

# Step 1: In-Place Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1

# Step 2: Optimized Bubble Sort
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if a swap occurred
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps occurred, the array is sorted
            break
    return arr

# Step 3: Hybrid Sort (using Insertion Sort for small subarrays)
def hybrid_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        return merge_sort(arr)  # Use Merge Sort for larger arrays

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Step 4: Visualization of Bubble Sort
def bubble_sort_with_visualization(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')

    ax.set_ylim(0, max(arr) + 10)
    plt.title("Bubble Sort Visualization")

    for i in range(n):
        for j in range(0, n - i - 1):
            for bar in bars:
                bar.set_color('blue')
            bars[j].set_color('red')
            bars[j + 1].set_color('red')

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            for bar, height in zip(bars, arr):
                bar.set_height(height)

            plt.pause(0.1)

    plt.show()

# Step 5: Compare and Test the Sorting Algorithms
def compare_sorting_algorithms(arr):
    algorithms = [
        ("In-Place Quick Sort", lambda x: quick_sort(x, 0, len(x) - 1)),
        ("Optimized Bubble Sort", optimized_bubble_sort),
        ("Hybrid Sort", hybrid_sort)
    ]

    for name, func in algorithms:
        arr_copy = arr.copy()
        func(arr_copy)
        print(f"{name} Result: {arr_copy}")

# Generate a random array
test_arr = [random.randint(1, 100) for _ in range(10)]
print("Original Array:", test_arr)

# Visualize Bubble Sort
bubble_sort_with_visualization(test_arr.copy())

# Compare the algorithms
compare_sorting_algorithms(test_arr.copy())
