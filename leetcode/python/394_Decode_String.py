class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        count_stack = []
        curr_str = ""
        k = 0
        for char in s:
            if char.isdigit():
                k = k * 10 + (ord(char) - ord('0'))
            elif char == '[':
                count_stack.append(k)
                stack.append(curr_str)
                k = 0
                curr_str = ""
            elif char == ']':
                n_times = count_stack.pop()
                decodedString = stack.pop()
                for i in range(n_times):
                    decodedString = decodedString + curr_str
                curr_str = decodedString
                
            else:
                curr_str += char
        
        return curr_str
