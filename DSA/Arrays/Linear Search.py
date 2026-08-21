"""
   Search for a target element using linear search.

   Returns the index of the first occurrence of target.
   Returns -1 if target is not present.

   Time Complexity: O(n)
   Space Complexity: O(1)
"""


def linear_search(nums, target):
    for index in range(len(nums)):
        if nums[index] == target:
            return index

    return -1


if __name__ == "__main__":
    nums = [4, 2, 7, 1, 9]
    target = 7

    result = linear_search(nums, target)
    print(f"Target {target} found at index: {result}")