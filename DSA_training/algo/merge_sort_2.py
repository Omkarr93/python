def merge_sort(arr):
    # Base Case: If the list has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge elements from both halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# Example Usage
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
# unsorted_list = [ 43, 3, 9]
sorted_list = merge_sort(unsorted_list)
print("Sorted List:", sorted_list)
