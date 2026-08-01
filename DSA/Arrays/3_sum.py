"""
3 Sum

Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k

nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets.
The output and the triplets can be returned in any order.
Example 1
Input: nums = [2, -2, 0, 3, -3, 5]
Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
"""

# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n^3)
# Space Complexity: O(n)

# ============================================================
def threeSum_brute(nums):
    n = len(nums)
    temp = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                summ = nums[i] + nums[j] + nums[k]

                if summ == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    temp.add(triplet)
    return [list(x) for x in temp]


# ============================================================

# Approach 2: Hash Map
# Time Complexity : O(n*n)
# Space Complexity: O(n)

# ============================================================

def threeSum_better(nums):
        temp = set()

        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                need = -(nums[i] + nums[j])
                if need in seen:
                    temp.add(tuple(sorted(([nums[i], nums[j], need]))))
                if nums[j] not in seen:
                    seen.add(nums[j])
        return [list(x) for x in temp]




# ============================================================

# Approach 3: Sorting + Two Pointers
#Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def threeSum_optimal(nums):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            k = n - 1
            j = i + 1

            while k > j:
                summ = nums[i] + nums[j] + nums[k]
                if summ > 0:
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
    return ans

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [2, -2, 0, 3, -3, 5]

    print("Brute Force :", threeSum_brute(nums))
    print("Better      :", threeSum_better(nums))
    print("Optimal     :", threeSum_optimal(nums))