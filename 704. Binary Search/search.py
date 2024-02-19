def search(self, nums: List[int], target: int) -> int:
    i = 0
    j = len(nums)-1
    while i<=j:
        m = (i+j)//2
        if target == nums[m]:
            return m
        elif target < nums[m]:
            j = m-1
        else:
            i = m+1
    return -1
