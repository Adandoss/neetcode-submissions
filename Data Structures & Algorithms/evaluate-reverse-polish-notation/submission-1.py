class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(first / second)
        return int(stack[0])
