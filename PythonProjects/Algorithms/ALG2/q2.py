def mergeC(array, temp_arr, left, mid, right):
    i = left  # Pointer to track the current index in the left subarray
    j = mid + 1  # Pointer to track the current index in the right subarray
    k = left  # Pointer for the temporary array where merged elements are stored
    inv_count = 0  # Initialize the inversion count for this merge step

    # Merge the two subarrays while counting inversions
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_arr[k] = array[i]  # Copy the smaller element from the left subarray
            i += 1
        else:
            temp_arr[k] = array[j]  # Copy the smaller element from the right subarray
            # Count inversions: All remaining elements in the left subarray are larger
            inv_count += (mid - i + 1)
            j += 1
        k += 1  # Move the pointer for the temporary array

    # Copy any remaining elements from the left subarray
    while i <= mid:
        temp_arr[k] = array[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j <= right:
        temp_arr[k] = array[j]
        j += 1
        k += 1

    # Copy the sorted and merged elements back to the original array
    for i in range(left, right + 1):
        array[i] = temp_arr[i]

    return inv_count  # Return the total number of inversions counted in this step

def mergeSC(arr, temp_arr, left, right):
    inv_count = 0  # Initialize the inversion count for the current range
    if left < right:
        mid = (left + right) // 2  # Find the midpoint to divide the array

        # Count inversions in the left half
        inv_count += mergeSC(arr, temp_arr, left, mid)

        # Count inversions in the right half
        inv_count += mergeSC(arr, temp_arr, mid + 1, right)

        # Count inversions while merging the two halves
        inv_count += mergeC(arr, temp_arr, left, mid, right)

    return inv_count

def inversions(array):
    n = len(array)
    tempArray = [0] * n  # Temporary array for merging
    return mergeSC(array, tempArray, 0, n - 1)

array = [94, 12, 46, 28, 60]
print("Number of inversions: ", inversions(array))
#Algorithm efficiently counts inversions in O(n log n) time and requires O(n) space.






