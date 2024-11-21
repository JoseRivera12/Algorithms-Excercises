
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) constant space not optimal number of operations
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         i += 1
        
        # while i < len(nums):
        #     nums[i] = 0
        #     i += 1
        # optimal solution
        last_not_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_not_zero], nums[i] = nums[i], nums[last_not_zero]
                last_not_zero += 1

