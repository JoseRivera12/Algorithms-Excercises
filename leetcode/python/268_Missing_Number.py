class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        # could be replaced by gauss formula expected_sum = len(nums)*len(nums+1)//2
        for i in range(len(nums) + 1):
            res += i

        return res - sum(nums) 
