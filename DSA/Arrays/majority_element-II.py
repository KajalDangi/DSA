"""
Majority Element II

Given an integer array nums of size n,
return all elements that appear more than n // 3 times.

The answer can contain at most two elements.

Example:
Input : [1, 2, 1, 1, 3, 2]
Output: [1]
"""

# ============================================================

# Approach 1: Linear Scan
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def majority_element_two_brute(nums):
    result = []

    for num in nums:

        if nums.count(num) > len(nums) // 3 and num not in result:
            result.append(num)

    return result

# ============================================================

# Approach 2: Hash Map
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def majority_element_two_better(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    result = []

    for num, count in frequency.items():

        if count > len(nums) // 3:
            result.append(num)

    return result

# ============================================================

# Approach 3: Extended Boyer-Moore Voting Algorithm
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def majority_element_two_optimal(nums):
    candidate1 = None
    candidate2 = None

    count1 = 0
    count2 = 0

    for num in nums:

        if count1 == 0 and candidate2 != num:
            candidate1 = num
            count1 = 1

        elif count2 == 0 and candidate1 != num:
            candidate2 = num
            count2 = 1

        elif num == candidate1:
            count1 += 1

        elif num == candidate2:
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    count1 = nums.count(candidate1)
    count2 = nums.count(candidate2)

    result = []

    if count1 > len(nums) // 3:
        result.append(candidate1)

    if candidate2 != candidate1 and count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

    print("Brute Force :", majority_element_two_brute(nums))
    print("Better      :", majority_element_two_better(nums))
    print("Optimal     :", majority_element_two_optimal(nums))




