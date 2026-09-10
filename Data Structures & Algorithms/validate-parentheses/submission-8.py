class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        for x in s:
            if x in ['(', '[', '{']:
                valid.append(x)
            else:
                if not valid:
                    return False
                stack_top = valid.pop()
                print(valid, stack_top)
                if x == ')':
                    if stack_top == '(':
                        continue
                    else:
                        return False
                if x == ']':
                    if stack_top == '[':
                        continue
                    else:
                        return False
                if x == '}':
                    if stack_top == '{':
                        continue
                    else:
                        return False
        if not valid:
            return True
        else:
            return False