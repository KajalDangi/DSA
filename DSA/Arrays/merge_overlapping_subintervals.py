"""
Merge Overlapping Intervals

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return the resulting intervals.
Example:
Input :
[[1,5],[3,6],[8,10],[15,18]]
Output:
    [[1,6],[8,10],[15,18]]
"""

# ============================================================

# Approach: Sorting + Greedy Merge
# Time Complexity : O(n log n)
# Space Complexity: O(n)

# ============================================================

def merge_overlap_optimal(intervals):
    intervals.sort()

    merged_intervals = []

    for interval in intervals:

        if not merged_intervals:
            merged_intervals.append(interval)

        elif interval[0] <= merged_intervals[-1][1]:

            merged_intervals[-1][1] = max(
                merged_intervals[-1][1],
                interval[1]
            )

        else:
            merged_intervals.append(interval)

    return merged_intervals


# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    intervals = [[1, 5], [3, 6], [8, 10], [15, 18]]

    print("Merged Intervals:")
    print(merge_overlap_optimal(intervals))

