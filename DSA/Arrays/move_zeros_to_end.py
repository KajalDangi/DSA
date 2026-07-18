"""
Move Zeroes

Given an integer array nums, move all 0's to the end while
maintaining the relative order of non-zero elements.

Example:
Input : [0, 1, 4, 0, 5, 2]
Output: [1, 4, 5, 2, 0, 0]
"""

# ============================================================

# Approach 1: Remove and Append
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def move_zeroes_brute(nums):
    zero_count = nums.count(0)
    while 0 in nums:
        nums.remove(0)
    nums.extend([0] * zero_count)

    return nums


# ============================================================

# Approach 2: Extra Array
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def move_zeroes_better(nums):
    non_zero_elements = []
    for num in nums:
        if num != 0:
            non_zero_elements.append(num)
    zero_count = len(nums) - len(non_zero_elements)
    non_zero_elements.extend([0] * zero_count)

    return non_zero_elements


# ============================================================

# Approach 3: Two Pointers (Optimal)
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def move_zeroes_optimal(nums):
    write_pointer = 0
    for read_pointer in range(len(nums)):

        if nums[read_pointer] != 0:
            nums[write_pointer], nums[read_pointer] = (
                nums[read_pointer],
                nums[write_pointer]
            )

            write_pointer += 1
    return nums


# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [0, 1, 4, 0, 5, 2]

    print("Brute Force :", move_zeroes_brute(nums[:]))
    print("Better      :", move_zeroes_better(nums[:]))
    print("Optimal     :", move_zeroes_optimal(nums[:]))