def union_array(nums1, nums2):
    """
    Find the union of two sorted arrays without duplicates.

    Both input arrays must be sorted.

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    n1 = len(nums1)
    n2 = len(nums2)

    i = 0
    j = 0
    union = []

    while i < n1 and j < n2:

        if nums1[i] > nums2[j]:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        else:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

    while i < n1:
        if not union or union[-1] != nums1[i]:
            union.append(nums1[i])
        i += 1

    while j < n2:
        if not union or union[-1] != nums2[j]:
            union.append(nums2[j])
        j += 1

    return union


if __name__ == "__main__":
    nums1 = [1, 2, 2, 3, 4]
    nums2 = [2, 3, 5, 6]

    print("Union:", union_array(nums1, nums2))