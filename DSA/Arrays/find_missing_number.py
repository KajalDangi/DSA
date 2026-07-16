#Given an integer array of size n containing distinct values in the range from 0 to n (inclusive),
# return the only number missing from the array within this range.


# --------------------------
# Approach 1: Infinit Looping
# Time: O(n²)
# Space: O(1)
# Brute
# --------------------------
def missingNumber(nums):
    i = 0
    while True:
        if i not in nums:
            return i
        else:
            i += 1



# --------------------------
# Approach 2: Hashing / Set
# Time:O(n)
# Space:O(n)
# Better
# --------------------------
def missingNumber(nums):
    s = set(nums)

    for x in range(len(nums) + 1):
        if x not in s:
            return x


# --------------------------
# Approach 3: Summation
# Time: O(n)
# Space: O(1)
# Optimal
# --------------------------
def missingNumber(nums):
    n = len(nums)
    return (n*(n+1))//2 -sum(nums)



# --------------------------


if __name__ == "__main__":
    nums = [0, 2, 3, 1, 4]
    print(missingNumber(nums))
    # Output : 5
