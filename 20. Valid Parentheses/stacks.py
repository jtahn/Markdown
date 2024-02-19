
def isValid(self, s: str) -> bool:
    brackets = {'(':')', '{':'}', '[':']'}
    stack = []
    for char in s:
        if char in brackets:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if char != brackets[stack.pop()]:
                return False
    return len(stack) == 0
