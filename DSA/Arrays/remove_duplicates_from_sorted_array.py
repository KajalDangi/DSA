# Given an integer array nums sorted in non-decreasing order,
# remove all duplicates in-place so that each unique element appears only once.

# --------------------------
# Approach 1: Sorting and Set
# Time: O(n log n )
# Space: O(n)
# Brute
# --------------------------
def removeDuplicates(nums):
     return len(sorted(list(set(nums))))

# --------------------------
# Approach 2:Extra Array
# Time:O(n)
# Space:O(n)
# Better
# --------------------------
def removeDuplicates(nums):
    temp = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            temp.append(nums[i])

    for i in range(len(temp)):
        nums[i] = temp[i]

    return len(temp)



# --------------------------
# Approach 3: Two Pointers
# Time: O(n)
# Space: O(1)
# Optimal
# --------------------------
def removeDuplicates(nums):
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums [i] = nums[j]
    return i+1



# --------------------------
if __name__ == "__main__":
    nums = [-2, 2, 4, 4, 4, 4, 5, 5]
    print(removeDuplicates(nums))
    # Output: 4
