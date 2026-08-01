# Given a binary array nums, return the maximum number of consecutive 1s in the array.

# --------------------------
# Approach 1: Generate all subarrays
# Time:O(n³)
# Space:O(n³)
# Brute
# --------------------------
def findMaxConsecutiveOnes(self, nums):
    sublists = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
    sublist1 = []
    for i in sublists:
        if len(i) == i.count(1):
            sublist1.append(i)
    if sublist1 == []:
        return 0
    else:
        return len(max(sublist1, key=len))

# --------------------------
# Approach 2: Store streak lengths
# Time: O(n)
# Space: O(n)
# Better
# --------------------------
def findMaxConsecutiveOnes(nums):
    bunch = []
    count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            bunch.append(count)
            count = 0

    bunch.append(count)

    return max(bunch)

# --------------------------
# Approach 3: Running max counter
# Time: O(n)
# Space: O(1)
#Optimal
# --------------------------
def findMaxConsecutiveOnes(nums):
    count = 0
    maximum = 0

    for num in nums:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum






# --------------------------
if __name__ == "__main__":
    nums = [1, 1, 0, 0, 1, 1, 1, 0]
    print(findMaxConsecutiveOnes(nums))
