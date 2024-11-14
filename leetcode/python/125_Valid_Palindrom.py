
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first approach 
        # s = s.lower()
        # s = ''.join([char for char in s if char.isalnum()])
        # print(s)
        # begin = 0
        # end = len(s) - 1
        # while begin < end:
        #     if s[begin] != s[end]:
        #         return False
        #     begin += 1
        #     end -= 1
        
        # return True
        # second approach
        begin = 0
        end = len(s) - 1
        
        while begin < end:
            while not s[begin].isalnum() and begin < end:
                begin += 1

            while not s[end].isalnum() and end > begin:
                end -= 1

            if s[end].lower() != s[begin].lower(): 
                return False
            
            begin += 1
            end -= 1
        
        return True
