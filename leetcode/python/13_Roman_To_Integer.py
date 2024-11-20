class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        last = 0
        res = 0
        for i in range(len(s) - 1, -1, - 1):
            val = mapping[s[i]]
            if val < last:
                res -= val
            else:
                res += val
            last = val
        
        return res
