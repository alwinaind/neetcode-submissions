class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        if not s:
            return True
        if len(s) == 1:
            return False
        for bracket in s:
            if bracket in '[{(':
                bracket_stack.append(bracket)
            else:
                if bracket_stack:
                    if (bracket == '}' and bracket_stack[-1] == '{') or (bracket == ']' and bracket_stack[-1] == '[') or (bracket == ')' and bracket_stack[-1] == '('):
                        bracket_stack.pop()
                    else:
                        return False
                else:
                    return False
        if bracket_stack:
            return False
        else:
            return True