"""Count Inversions

Striver A2Z Sheet
Difficulty: Hard

Given an integer array nums. Return the number of inversions in the array.

Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.

Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5"""

# ============================================================

# Approach 1: Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(1)

# ============================================================
def numberOfInversions_brute(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                count+=1
    return count



# ============================================================

# Approach 2: Merge Sort (Optimal)
# Time Complexity : O(n log n)
# Space Complexity: O(n)

# ============================================================
def numberOfInversions_optimal(nums):
    def merge(nums,low,mid,high):
        left = low
        right = mid+1
        temp = []
        count = 0
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
                count += (mid - left + 1)

        if left <= mid:
            temp.extend(nums[left:mid+1])
        if right <= high:
            temp.extend(nums[right:high+1])

        x = 0
        while low < high+1:
            nums[low] = temp[x]
            low+=1
            x+=1

        return count



    def merge_sort(nums,low,high):
        if low >= high:
            return 0
        mid = (low+high)//2
        left_count = merge_sort(nums,low,mid)
        right_count = merge_sort(nums,mid+1,high)
        merge_count = merge(nums,low,mid,high)
        return left_count + right_count + merge_count




    n = len(nums)
    low = 0
    high = n-1
    return merge_sort(nums,low,high)

# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    nums = [2, 3, 7, 1, 3, 5]
    print("Brute Force :", numberOfInversions_brute(nums[:]))
    print("Optimal     :", numberOfInversions_optimal(nums[:]))



