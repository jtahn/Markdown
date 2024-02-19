def maxSubArray(self, nums: List[int]) -> int:
    max_right_sum_seen = -math.inf
    max_sum_seen = -math.inf
    for num in nums:
        max_right_sum_seen = num + max(0, max_right_sum_seen)
        max_sum_seen = max(max_sum_seen, max_right_sum_seen)
    return max_sum_seen
