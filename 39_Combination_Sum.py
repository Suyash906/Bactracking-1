class Solution:
    def __helper(self, candidates, target, index, curr_sum, curr_list, result):
        ## base
        if curr_sum == target:
            result.append(curr_list[:])
            return
        
        if curr_sum > target:
            return
        
        ## body
        for i in range(index, len(candidates)):
            curr_sum += candidates[i]
            curr_list.append(candidates[i])
            
            self.__helper(candidates, target, i, curr_sum, curr_list, result)
            
            curr_sum -= candidates[i]
            curr_list.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.__helper(candidates, target, 0, 0, [], result)
        return result
