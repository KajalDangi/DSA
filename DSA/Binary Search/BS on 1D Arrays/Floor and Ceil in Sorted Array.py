"""
Find the floor and ceil of x in a sorted array.

Floor: Greatest value <= x
Ceil: Smallest value >= x

Returns:
    [floor, ceil]

If floor or ceil does not exist, returns -1 for that value.

Time Complexity: O(log n)
Space Complexity: O(1)
"""



def get_floor_and_ceil(nums, x):
    low = 0
    high = len(nums) - 1

    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            return [x, x]

        if nums[mid] < x:
            floor = nums[mid]
            low = mid + 1
        else:
            ceil = nums[mid]
            high = mid - 1

    return [floor, ceil]


if __name__ == "__main__":
    nums = [1, 2, 4, 6, 8, 10]
    x = 5

    print(f"Floor and Ceil of {x}: {get_floor_and_ceil(nums, x)}")