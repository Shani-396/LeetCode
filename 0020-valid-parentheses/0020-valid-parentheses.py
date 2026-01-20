class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ('(', '[', '{')
        closedBrackets = (')', ']', '}')
        dict = { '(': ')', '[': ']', '{': '}' }
        stack = []
        for char in s:
            if char in openBrackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                if dict[stack.pop()] != char:
                    return False
        return len(stack) == 0
        