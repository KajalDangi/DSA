#Given an integer array nums, rotate the array to the left by one.


# --------------------------
# Approach 1: Array Slicing / Extra Array
# Time: O(n)
# Space: O(n)
# Brute
# --------------------------
def rotateArrayByOne(nums):
    return nums[1:] + [nums[0]]

# --------------------------
# Approach 2: Temporary Array
# Time: O(n)
# Space: O(n)
# Better
# --------------------------

def rotateArrayByOne(nums):
    temp = []

    for i in range(1, len(nums)):
        temp.append(nums[i])

    temp.append(nums[0])

    return temp


# --------------------------
# Approach 3: In-Place Shift
# Time: O(n)
# Space: O(1)
# Optimal
# --------------------------
def rotateArrayByOne(nums):
    temp = nums[0]
    for j in range(1,len(nums)):
        nums[j-1] = nums[j]
    nums[-1] = temp
    return nums







# --------------------------
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(rotateArrayByOne(nums))
    # Output: [2, 3, 4, 5, 1]
