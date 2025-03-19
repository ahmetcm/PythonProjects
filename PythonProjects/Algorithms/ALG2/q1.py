def maxCross(arr, left, mid, right):
    # Initialize left_sum to negative infinity to handle the case where all elements are negative
    left_sum = float('-inf')
    current_sum = 0

    # Traverse the left half of the array to find the maximum sum crossing the middle from left to mid
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]  # Add current element to current_sum
        left_sum = max(left_sum, current_sum)  # Update left_sum if current_sum is larger

    # Initialize right_sum to negative infinity to handle the case where all elements are negative
    right_sum = float('-inf')
    current_sum = 0

    # Traverse the right half of the array to find the maximum sum crossing the middle from mid+1 to right
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    # Return the sum of the left and right sums, which represents the maximum sum crossing the middle
    return left_sum + right_sum


# This function recursively computes the maximum subarray sum using divide and conquer
def maxSub(array, l, r):
    if l == r:
        return array[l]

    # Find the middle index of the array
    mid = (l + r) // 2

    # Recursively find the maximum sum in the left half of the array
    left_max = maxSub(array, l, mid)

    # Recursively find the maximum sum in the right half of the array
    right_max = maxSub(array, mid + 1, r)

    # Find the maximum sum of the subarray that crosses the middle
    cross_max = maxCross(array, l, mid, r)

    return max(left_max, right_max, cross_max)


# Test array
array = [62, -42, 64, -31, 80, -120, 43, -23, 10]

n = len(array)

result = maxSub(array, 0, n - 1)

print("Maximum Subarray Sum:", result)
