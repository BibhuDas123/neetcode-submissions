class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1=set(nums)
        if len(nums)==len(d1):
            return False
        else:
            return True
         