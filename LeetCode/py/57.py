"""direct"""
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0               # intervals[:i] will be strictly left oldIntervals
    j = len(intervals)  # intervals[j:] will be strictly right oldIntervals
    for k in range(len(intervals)):
        interval = intervals[k]
        if interval[1] < newInterval[0]:
            i=k+1
        elif newInterval[1] < interval[0]:
            j = k
            break
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    return intervals[:i] + [newInterval] + intervals[j:]