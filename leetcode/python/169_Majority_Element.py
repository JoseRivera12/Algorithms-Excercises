class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # easy solution
        # linear time
        # linear space
        # mapping = {}
        # for num in nums:
        #     if num in mapping:
        #         mapping[num] += 1
        #     else:
        #         mapping[num] = 1

        # m = len(nums) / 2
        # for key, val in mapping.items():
        #     if val >= m:
        #         return key
        
        # return -1
        # better approach
        res = -1
        count = 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1
        
        return res
