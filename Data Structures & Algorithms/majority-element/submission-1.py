class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        canditate=None
        for num in nums:
            if count==0:
                canditate=num
            count+=(1 if num==canditate else -1)
        return canditate
        