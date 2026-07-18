"""
Sort an Array of 0s, 1s and 2s

Given an array nums consisting only of 0s, 1s, and 2s,
sort the array in non-decreasing order.
The sorting must be done in-place.
Example:
Input : [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
"""

# ============================================================

# Approach 1: Basic Sorting
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def sort_zero_one_two_brute(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

# ============================================================

# Approach 2: Counting Frequency
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def sort_zero_one_two_better(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    zero_count = frequency.get(0, 0)
    one_count = frequency.get(1, 0)
    two_count = frequency.get(2, 0)

    for i in range(zero_count):
        nums[i] = 0

    for i in range(zero_count, zero_count + one_count):
        nums[i] = 1

    for i in range(zero_count + one_count, len(nums)):
        nums[i] = 2

    return nums

# ============================================================

# Approach 3: Dutch National Flag Algorithm
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def sort_zero_one_two_optimal(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:

            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1
            mid += 1

        elif nums[mid] == 1:

            mid += 1

        else:

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

    return nums

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [1, 0, 2, 1, 0]

    print("Brute Force :", sort_zero_one_two_brute(nums[:]))
    print("Better      :", sort_zero_one_two_better(nums[:]))
    print("Optimal     :", sort_zero_one_two_optimal(nums[:]))


