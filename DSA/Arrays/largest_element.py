# Given an array of integers nums, return the largest element.

# ---------------------------
# Approach 1: Sorting
# Time: O(n log n)
# Space: O(n)
# Better
# ---------------------------

def largestElement(nums):
    sort_num = sorted(nums)
    return sort_num[-1]



# ---------------------------
# Approach 2: max() Function
# Time: O(n)
# Space: O(1)
# Library Function
# ---------------------------
def largestElement(nums):
    return max(nums)



# ---------------------------
# Approach 3: Linear Scan
# Time: O(n)
# Space: O(1)
# Optimal
# ---------------------------
def largestElement(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest



# ---------------------------
if __name__ == "__main__":
    nums = [3, 3, 6, 1]
    print(largestElement(nums))   # Output: 6
