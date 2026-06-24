class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {"(" : ")", "[" : "]", "{" : "}"}

        for c in s:
            if c in brackets_dict.keys():
                stack.append(c)
            else:
                if stack and brackets_dict[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

        