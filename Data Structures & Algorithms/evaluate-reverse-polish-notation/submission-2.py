class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = []
        for token in tokens:
            if token == '+':
                res = operations.pop()
                res = operations.pop() + res
                operations.append(int(res))
            elif token == '-':
                res = operations.pop()
                res = operations.pop() - res 
                operations.append(int(res))
            elif token == '*':
                res = operations.pop()
                res = operations.pop() * res 
                operations.append(int(res))
            elif token =='/':
                res = operations.pop()
                res = operations.pop()/res
                operations.append(int(res))
            else:
                operations.append(int(token))        
        return operations[0]
            
                
                