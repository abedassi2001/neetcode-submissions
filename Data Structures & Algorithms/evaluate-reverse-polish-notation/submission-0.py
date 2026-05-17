from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        signs = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in signs:
                # If it's a number, convert to int and push to stack
                stack.append(int(token))
            else:
                # If it's an operator, pop the top two numbers
                # Note: b is popped first because it was pushed last (Right operand)
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # LeetCode specifies truncation toward zero for division
                    stack.append(int(a / b))
        
        # The final remaining item on the stack is our total result
        return stack.pop()