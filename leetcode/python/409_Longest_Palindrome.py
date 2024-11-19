cclass Solution:
    def longestPalindrome(self, s: str) -> int:
        # first approach
        # letters = Counter(s)
        # ans = 0
        # has_even = False

        # for num in letters.values():
        #     if num % 2 == 0:
        #         ans += num
        #     else:
        #         ans += num - 1
        #         has_even = True
        
        # if has_even:
        #     ans += 1

        # return ans

        # better one
        letters = set()
        res = 0

        for c in s:
            if c in letters:
                letters.remove(c)
                res += 2
            else:
                letters.add(c)

        if letters:
            res += 1

        return reslass Solution:
    def longestPalindrome(self, s: str) -> int:
        # first approach
        # letters = Counter(s)
        # ans = 0
        # has_even = False

        # for num in letters.values():
        #     if num % 2 == 0:
        #         ans += num
        #     else:
        #         ans += num - 1
        #         has_even = True
        
        # if has_even:
        #     ans += 1

        # return ans

        # better one
        letters = set()
        res = 0

        for c in s:
            if c in letters:
                letters.remove(c)
                res += 2
            else:
                letters.add(c)

        if letters:
            res += 1

        return res
