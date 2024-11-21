class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initial solution O(N . M) Space is constant
        # initial_word = strs[0]
        # res = ""
        # flag = False
        # for i in range(len(initial_word)):
        #     for j in range(1, len(strs)):
        #         if i < len(strs[j]):
        #             print(strs[j], strs[j][i])
        #             if initial_word[i] != strs[j][i]:
        #                 flag = True
        #                 break
        #         else:
        #             flag = True
        #             break
        #     if flag:
        #         return res
        #     else:
        #         res += initial_word[i]
        
        # return res
        # improved solution O(N . M) Space is constant
        # if not strs:
        #     return ""
        
        # initial = strs[0]
        # for i in range(len(initial)):
        #     char = initial[i]
        #     for word in strs[1:]:
        #         if i >= len(word) or word[i] != char:
        #             return initial[:i]

        # return initial
        # binary search O(N . M . log(m)) Space is constant
        if not strs:
            return ""
        
        min_len = min(len(word) for word in strs)
        low, high = 1, min_len
        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return strs[0][: (low + high) // 2]

    def isCommonPrefix(self, strs: List[str], pos: int) -> bool:
        char = strs[0][:pos]
        for word in strs[1:]:
            if not word.startswith(char):
                return False
        
        return True
