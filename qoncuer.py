import random

# Step 1: Generate random numbers
random.seed(40)
data = [random.randint(0, 100) for _ in range(100)]

# Step 2: Define the conquer method (QuickSort)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    # Recursively sort left and right, then combine
    return quicksort(left) + middle + quicksort(right)

# Step 3: Sort the data
sorted_data = quicksort(data)

# Output the results
print("Original Data:", data)
print("\nSorted Data:", sorted_data)
