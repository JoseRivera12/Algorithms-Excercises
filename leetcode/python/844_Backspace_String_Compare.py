class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for letter in s:
            if letter != '#':
                s_stack.append(letter)
            elif s_stack:
                s_stack.pop()
                
        t_stack = []
        for letter in t:
            if letter != '#':
                t_stack.append(letter)
            elif t_stack:
                t_stack.pop()
        
        
        return ''.join(s_stack) == ''.join(t_stack)
