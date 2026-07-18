"""
Two Sum

Given an array of integers nums and an integer target,
return the indices of two numbers such that they add up
to target.

Each input has exactly one solution, and the same element
cannot be used twice.

Example:
Input : nums = [1, 6, 2, 10, 3]
Target: 7
Output: [0, 1]
"""

# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [i, j]




# ============================================================

# Approach 2: Hash Map (Optimal)
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def two_sum_optimal(nums, target):
    seen = {}
    for index, value in enumerate(nums):

        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index




# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [1, 6, 2, 10, 3]
    target = 7

    print("Brute Force :", two_sum_brute(nums, target))
    print("Optimal     :", two_sum_optimal(nums, target))



