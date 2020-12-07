class Solution:
    def __helper(self, num, target, index, calc, tail, expression, result):
        ## base
        if index == len(num):
            if calc == target:
                # print(expression)
                result.append("".join(expression))
            return
        
        ## body
        
        for i in range(index, len(num)):
            if num[index] == '0' and i != index:
                continue
            curr = int(num[index:i+1])
            if index == 0:
                self.__helper(num, target, i + 1, curr, curr, expression + [num[index:i+1]], result)
            else:
                expression.append('+')
                expression.append(num[index:i+1])
                self.__helper(num, target, i + 1, calc + curr, curr, expression, result)
                expression.pop()
                expression.pop()
                
                expression.append('-')
                expression.append(num[index:i+1])
                self.__helper(num, target, i + 1, calc - curr, -curr, expression, result)
                expression.pop()
                expression.pop()
                
                expression.append('*')
                expression.append(num[index:i+1])
                self.__helper(num, target, i + 1, calc - tail + curr * tail, curr * tail, expression, result)
                expression.pop()
                expression.pop()
            
    
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.__helper(num, target, 0, 0, 0, [], result)
        return result
