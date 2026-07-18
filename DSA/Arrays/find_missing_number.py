"""
Missing Number

Given an integer array nums containing n distinct numbers
in the range [0, n], return the only number missing from
the array.

Example:
Input : [0, 2, 3, 1, 4]
Output: 5
"""


# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def missing_number_brute(nums):
     candidate = 0
     while True:
         if candidate not in nums:
             return candidate

         candidate += 1



# ============================================================

# Approach 2: Hash Set
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def missing_number_better(nums):
     values = set(nums)
     for number in range(len(nums) + 1):
         if number not in values:
             return number

# ============================================================

# Approach 3: Summation Formula
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def missing_number_optimal(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# ============================================================

# Approach 3: XOR
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def missing_number_xor(nums):
        n = len(nums)
        xor1 = 0
        xor2 = 0
        for i in range(n + 1):
            xor1 = xor1 ^ i
        for num in nums:
            xor2 = xor2 ^ num

        return xor1 ^ xor2

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [0, 2, 3, 1, 4]
    print("Brute Force :", missing_number_brute(nums))
    print("Better      :", missing_number_better(nums))
    print("Optimal     :", missing_number_optimal(nums))
    print("XOR         :", missing_number_xor(nums))




