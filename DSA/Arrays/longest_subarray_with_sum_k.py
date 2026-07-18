"""
Longest Subarray with Sum K

Given an array nums of size n and an integer k,
find the length of the longest subarray whose sum equals k.

If no such subarray exists, return 0.

Example:
Input :
nums = [10, 5, 2, 7, 1, 9]
k = 15


Output:4

Explanation:
    [5, 2, 7, 1] has sum = 15

"""

# ============================================================

# Approach 1: Generate All Subarrays
# Time Complexity : O(n³)
# Space Complexity: O(n³)

# ============================================================

def longest_subarray_brute(nums, k):
    longest_length = 0
    subarrays = [
    nums[i:j]
    for i in range(len(nums))
    for j in range(i + 1, len(nums) + 1)]

    for subarray in subarrays:
        if sum(subarray) == k:
            longest_length = max(longest_length, len(subarray))

    return longest_length
# ============================================================

# Approach 2: Check Larger Lengths First
# Time Complexity : O(n³)
# Space Complexity: O(n)

# ============================================================

def longest_subarray_improved(nums, k):
    n = len(nums)
    current_length = n
    while current_length > 0:

        for start in range(n - current_length + 1):

            subarray = nums[start:start + current_length]

            if sum(subarray) == k:
                return current_length

        current_length -= 1

    return 0

# ============================================================

# Approach 3: Prefix Sum + Hash Map (Optimal)
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def longest_subarray_optimal(nums, k):
    prefix_index = {}

    prefix_sum = 0
    longest_length = 0

    for index, value in enumerate(nums):

        prefix_sum += value

        if prefix_sum == k:
            longest_length = index + 1

        remainder = prefix_sum - k

        if remainder in prefix_index:
            longest_length = max(
                longest_length,
                index - prefix_index[remainder]
            )

        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = index

    return longest_length





# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15

    print("Brute Force :", longest_subarray_brute(nums, k))
    print("Improved    :", longest_subarray_improved(nums, k))
    print("Optimal     :", longest_subarray_optimal(nums, k))



