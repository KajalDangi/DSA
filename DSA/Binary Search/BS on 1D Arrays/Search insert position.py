"""
Find the index where target is present or should be inserted
to maintain sorted order.

The input array must be sorted.

Time Complexity: O(log n)
Space Complexity: O(1)
"""



def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5

    print(f"Insert position of {target}: {search_insert(nums, target)}")