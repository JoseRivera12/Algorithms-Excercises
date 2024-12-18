class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i = 0
        j = n - 1

        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] * nums[i]
                i += 1
            else:
                res[k] = nums[j] * nums[j]
                j -= 1

        return res 


        
