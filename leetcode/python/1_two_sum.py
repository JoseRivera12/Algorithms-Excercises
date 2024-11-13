class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i, value in enumerate(nums):
            search = target - value
            if search in memory:
                return [i, memory[search]]
            else:
                memory[value] = i

        return [-1, -1]

"""
assumptions
 1. Exactly one solution.
 2. You can't use the same element twice
memory = {2:0,}
target = 9
i = 0
curr = 2
search = curr - target 

"""
