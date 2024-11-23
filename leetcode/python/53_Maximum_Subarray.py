
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP iterative
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # max_sum = dp[0]

        # for i in range(1, n):
        #     dp[i] = max(nums[i], dp[i-1] + nums[i])
        #     max_sum = max(max_sum, dp[i])
        
        # return max_sum

        # DP recursive
        # memo = {}

        # def maxEndingAt(i):
        #     if i == 0:
        #         memo[0] = nums[0]
        #         return nums[0]

        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i], maxEndingAt(i - 1) + nums[i])

        #     return memo[i]
        
        # global_max = float('-inf')
        # for i in range(len(nums)):
        #     global_max = max(maxEndingAt(i), global_max)
        
        # return global_max
        # bottom up iterative optimized
        max_ending_here = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            global_max = max(global_max, max_ending_here)
        
        return global_max
