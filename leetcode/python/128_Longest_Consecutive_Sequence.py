class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        unique = set(nums)
        lcs = 1
        
        for num in unique:
            if num - 1 not in unique:
                curr_max = 1
                curr_num = num + 1
                while curr_num in unique:
                    curr_num += 1
                    curr_max += 1
                lcs = max(lcs, curr_max)
        
        return lcs
