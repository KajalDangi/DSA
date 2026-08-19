"""
Find the first index where nums[index] > x.

The input array must be sorted.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def upper_bound(nums, x):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    nums = [1, 2, 4, 4, 5, 7]
    x = 4

    print(f"Upper bound of {x}: index {upper_bound(nums, x)}")