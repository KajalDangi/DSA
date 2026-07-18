"""
Remove Duplicates from Sorted Array

Given a sorted integer array nums, remove duplicates in-place
such that each unique element appears only once.

Return the number of unique elements.
Example:
Input : [0, 0, 3, 3, 5, 6]
Output: 4

Unique elements:
[0, 3, 5, 6]
"""

# ============================================================

# Approach 1: Set
# Time Complexity : O(n log n)
# Space Complexity: O(n)

# ============================================================

def remove_duplicates_brute(nums):
    unique_values = sorted(set(nums))
    return len(unique_values)

"""
Note:
Returns the count of unique elements but does not
satisfy the in-place requirement.
"""


# ============================================================

# Approach 2: Extra Array
# Time Complexity : O(n)
# Space Complexity: O(n)

# ============================================================

def remove_duplicates_better(nums):
    unique_values = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique_values.append(nums[i])

    for i in range(len(unique_values)):
        nums[i] = unique_values[i]

    return len(unique_values)



# ============================================================

# Approach 3: Two Pointers (Optimal)
# Time Complexity : O(n)
# Space Complexity: O(1)

# ============================================================

def remove_duplicates_optimal(nums):
    write_pointer = 0
    for read_pointer in range(1, len(nums)):

        if nums[read_pointer] != nums[write_pointer]:
            write_pointer += 1
            nums[write_pointer] = nums[read_pointer]

    return write_pointer + 1




# ============================================================

# Driver Code

# ============================================================

if __name__ == "__main__":
    nums = [-2, 2, 4, 4, 4, 4, 5, 5]

    print("Brute Force :", remove_duplicates_brute(nums[:]))
    print("Better      :", remove_duplicates_better(nums[:]))
    print("Optimal     :", remove_duplicates_optimal(nums[:]))


