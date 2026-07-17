"""
Single Number
Given a non-empty array of integers, every element appears
twice except for one. Find that single number.

Example:
Input : [1, 2, 2, 4, 3, 1, 4]
Output: 3
"""

# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def single_number_brute(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num



# ============================================================

# Approach 2: Hash Map
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def single_number_better(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    for num, count in frequency.items():
        if count == 1:
            return num





# ============================================================

# Approach 3: XOR
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def single_number_optimal(nums):
          return 0


# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [1, 2, 2, 4, 3, 1, 4]

    print("Brute Force :", single_number_brute(nums))
    print("Better      :", single_number_better(nums))
    print("Optimal     :", single_number_optimal(nums))



