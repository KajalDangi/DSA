#Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

# --------------------------
# Approach 1: Array Slicing / Extra Array
# Time: O(n)
# Space: O(n)
# Brute
# --------------------------
def rotateArray(nums,k):
    k = k % len(nums)
    return nums[k:] + nums[:k]



# --------------------------
# Approach 2: Linear Scan and Shifting
# Time: O(n)
# Space: O(k)
# Better
# --------------------------
def rotateArray(nums,k):
    k = k % len(nums)
    temp =[]
    for i in range(k):
        temp.append(nums[i])
    for j in range(k,len(nums)):
        nums[j-k] = nums[j]
    m = 0
    for n in range(len(nums)-k,len(nums)):
        nums[n] = temp[m]
        m+=1
    return nums


# --------------------------
# Approach 3: Reversal Algorithm (your Python slicing version)
# Time: O(n)
# Space: O(n)
# Better
# --------------------------
def rotateArray(nums,k):
    k = k % len(nums)
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    nums[:]  = nums[:][::-1]
    return nums


# --------------------------
# Approach 4: Reversal Algorithm (true in-place reverse)
# Time: O(n)
# Space: O(1)
# Optimal
# --------------------------
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
def rotateArray(nums, k):
    n = len(nums)
    k %= n

    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    reverse(nums, 0, n - 1)

    return nums














if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    print(rotateArray(nums,k))
    # Output: [3, 4, 5, 6, 1, 2]
