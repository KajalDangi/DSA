"""
4 Sum

Given an integer array nums and an integer target.
Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.
Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets.
The output and the quadruplets can be returned in any order.

Example 1
Input: nums = [1, -2, 3, 5, 7, 9], target = 7
Output: [[-2, 1, 3, 5]]
"""

# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n^4)
# Space Complexity: O(number of unique quadruplets)

# ============================================================
def fourSum_brute(nums, target):
    temp = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for x in range(k + 1, n):
                    summ = nums[i] + nums[j] + nums[k] + nums[x]
                    if summ == target:
                        temp.add(tuple(sorted([nums[i], nums[j], nums[k], nums[x]])))
    return [list(x) for x in temp]


# ============================================================

# Approach 2: Hash Map
# Time Complexity : O(n³)
# Space Complexity: O(n)

# ============================================================

def fourSum_better(nums, target):
        temp = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    need = target - (nums[i] + nums[j] + nums[k])

                    if need in seen:
                        q = tuple(sorted([nums[i], nums[j], nums[k], need]))
                        temp.add(q)
                    if nums[k] not in seen:
                        seen.add(nums[k])
        return [list(x) for x in temp]




# ============================================================

# Approach 3: Sorting + Two Pointers
# Time Complexity : O(n³)
# Space Complexity: O(1)

# ============================================================

def fourSum_optimal(nums, target):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                else:
                    k = j + 1
                    x = n - 1
                    need = target - (nums[i] + nums[j])
                    while k < x:
                        summ = nums[x] + nums[k]
                        if summ < need:
                            k += 1
                        elif summ > need:
                            x -= 1
                        else:
                            ans.append([nums[i], nums[j], nums[k], nums[x]])
                            k += 1
                            x -= 1
                            while k < x and nums[k] == nums[k - 1]:
                                k += 1
                            while k < x and nums[x] == nums[x + 1]:
                                x -= 1
    return ans

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [1, -2, 3, 5, 7, 9]
    target = 7


    print("Brute Force :", fourSum_brute(nums, target))
    print("Better      :", fourSum_better(nums, target))
    print("Optimal     :", fourSum_optimal(nums, target))