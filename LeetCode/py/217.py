"""hashing"""
def containsDuplicate(self, nums: List[int]) -> bool:
    h = set()
    for n in nums:
        if n in h:
            return True
        else:
            h.add(n)
    return False


"""sorting"""
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
