import math
import random
import time

def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

def linear_search_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


def compare_search_algorithms(arr, target):
    print(f"\nSearching for target: {target}")
    
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_count(arr, target)
    linear_time = time.time() - start_time
    
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_count(arr_sorted, target)
    binary_time = time.time() - start_time
    
    start_time = time.time()
    jump_result = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Time: {jump_time:.6f} seconds")

def main():
    test_list = [random.randint(1, 100) for _ in range(20)]
    sorted_list = sorted(test_list)
    
    print("Original list:", test_list)
    print("Sorted list:", sorted_list)
    
    target = random.choice(test_list)
    print(f"\nSearching for: {target}")

    indices = linear_search_all_indices(test_list, target)
    print(f"Linear Search (All Indices): Target found at indices {indices}")
    
    linear_result, linear_comparisons = linear_search_count(test_list, target)
    print(f"Linear Search (Comparison Count): Found at index {linear_result}, Comparisons: {linear_comparisons}")
    
    insertion_point = binary_search_insertion_point(sorted_list, target)
    print(f"Binary Search (Insertion Point): Target should be inserted at index {insertion_point}")
    
    binary_result = binary_search(sorted_list, target)
    print(f"Binary Search (Iterative): Found at index {binary_result}")
    
    binary_recursive_result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (Recursive): Found at index {binary_recursive_result}")

    jump_result = jump_search(sorted_list, target)
    print(f"Jump Search: Found at index {jump_result}")
    
    print("\nPerformance Comparison with Larger List:")
    large_list = list(range(100000))
    compare_search_algorithms(large_list, 99999)

if __name__ == "__main__":
    main()
