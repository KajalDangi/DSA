"""
Search for a target in a sorted array using binary search.

Time Complexity: O(log n)
Space Complexity: O(1)
    """



def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    result = binary_search(nums, target)
    print(f"Target {target} found at index: {result}")