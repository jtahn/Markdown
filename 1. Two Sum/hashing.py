def twoSum(self, nums: List[int], target: int) -> List[int]:
    found = {}
    for i in range(len(nums)):
        a = nums[i]
        if target-a in found:
            return [i,found[target-a]]
        else:
            found[a] = i
    return
