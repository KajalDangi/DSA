# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


# --------------------------
# Approach 1: Sorting
# Time: O(n log n)
# Space: O(n)
# Better
# --------------------------
def isSorted(nums):
    if nums == sorted(nums):
        return "true"
    return "false"



# --------------------------
# Approach 2: Linear Scan
# Time: O(n)
# Space: O(1)
# Optimal
# --------------------------
def isSorted(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return "false"
    return "true"




# --------------------------
if __name__ == "__main__":
    nums = [1, 2, 1, 4, 5]

    print(isSorted(nums))

       # Output: false
