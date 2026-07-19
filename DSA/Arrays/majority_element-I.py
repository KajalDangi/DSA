"""
Majority Element

Given an integer array nums of size n, return the majority element.
The majority element is the element that appears more than n // 2 times.
It is guaranteed that a majority element exists.

Example:
Input : [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7
"""

# ============================================================

# Approach 1: Linear Scan
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def majority_element_brute(nums):
    n = len(nums)

    for num in nums:

        if nums.count(num) > n // 2:
            return num

# ============================================================

# Approach 2: Hash Map
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def majority_element_better(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    for num, count in frequency.items():

        if count > len(nums) // 2:
            return num
# ============================================================

# Approach 3: Boyer-Moore Voting Algorithm
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def majority_element_optimal(nums):
    candidate = None
    count = 0

    for num in nums:

        if count == 0:
            candidate = num
            count = 1

        elif num == candidate:
            count += 1

        else:
            count -= 1

    return candidate

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

    print("Brute Force :", majority_element_brute(nums))
    print("Better      :", majority_element_better(nums))
    print("Optimal     :", majority_element_optimal(nums))

