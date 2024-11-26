class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num1, num2 = stack.pop(), stack.pop()
                operation = operations[token]
                stack.append(operation(num2, num1))
        
        return stack.pop()
