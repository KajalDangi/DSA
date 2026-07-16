"""
LeetCode 493 - Reverse Pairs
Problem:
Given an integer array nums, return the number of reverse pairs.

A reverse pair is defined as:
(i, j) such that:
0 <= i < j < len(nums)
nums[i] > 2 * nums[j]

Example:
Input:  [6, 4, 1, 2, 7]
Output: 3
"""
# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================

def reverse_pairs_brute(nums):
     count = 0
     n = len(nums)
     for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1

     return count


# ============================================================

# Approach 2: Merge Sort (Optimal)
# Time Complexity : O(n log n)
# Space Complexity: O(n)

# ============================================================

def reverse_pairs(nums):
    def count_pairs(nums, low, mid, high):
        """
        Count reverse pairs between two sorted halves:
        nums[low ... mid]
        nums[mid+1 ... high]
        """
        count = 0
        right = mid + 1

        for left in range(low, mid + 1):

            while right <= high and nums[left] > 2 * nums[right]:
                right += 1

            count += right - (mid + 1)

        return count

    def merge(nums, low, mid, high):
        """
        Merge two sorted halves.
        """
        left = low
        right = mid + 1

        temp = []

        while left <= mid and right <= high:

            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        temp.extend(nums[left:mid + 1])
        temp.extend(nums[right:high + 1])

        for i in range(len(temp)):
            nums[low + i] = temp[i]

    def merge_sort(nums, low, high):

        if low >= high:
            return 0

        mid = (low + high) // 2

        left_pairs = merge_sort(nums, low, mid)
        right_pairs = merge_sort(nums, mid + 1, high)

        current_pairs = count_pairs(nums, low, mid, high)

        merge(nums, low, mid, high)

        return left_pairs + right_pairs + current_pairs


    return merge_sort(nums, 0, len(nums) - 1)




# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [6, 4, 1, 2, 7]
    print("Brute Force :", reverse_pairs_brute(nums[:]))
    print("Optimal     :", reverse_pairs(nums[:]))




