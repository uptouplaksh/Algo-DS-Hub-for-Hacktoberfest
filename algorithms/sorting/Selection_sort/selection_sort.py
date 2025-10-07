def selection_sort(arr):
    """
    Sorts a list using the selection sort algorithm.
    Args:
        arr: The list to be sorted.
    """
    n = len(arr)
    for i in range(n):
        # Assume the current element is the minimum
        min_index = i
        
        # Iterate through the unsorted portion to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element if they are different
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Example :
my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)
selection_sort(my_list)
print("Sorted list:", my_list) 
