# Given an array of integers nums, return the second-largest element in the array.
# If the second-largest element does not exist, return -1.

# --------------------------
# Approach 1: Sorting and set
# Time: O(n log n)
# Space: O(n)
# Brute
# --------------------------
def secondLargestElement(nums):
     temp_nums = sorted(list(set(nums)))
     if len(temp_nums) > 1:
         return temp_nums[-2]
     else:
         return -1

# --------------------------
# Approach 2: max() Function and linear scan
# Time: O(n)
# Space: O(1)
# Better
# --------------------------
def secondLargestElement(nums):
    largest = max(nums)
    second_largest = -1
    for num in nums:
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest



# --------------------------
# Approach 3:
# Time:
# Space:
# --------------------------



# --------------------------
if  __name__ == "__main__":
    nums = [8, 8, 7, 6, 5]
    print(secondLargestElement(nums)) #Output = 7