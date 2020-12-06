class Solution:
    def __helper(self, candidates, target, index, curr_sum, curr_list, result):
        ## base
        if curr_sum == target:
            result.append(curr_list)
            return
        
        if curr_sum > target or index == len(candidates):
            return
        
        ## body
        self.__helper(candidates, target, index + 1, curr_sum, curr_list[:], result)
        
        self.__helper(candidates, target, index, curr_sum + candidates[index], curr_list[:] + [candidates[index]], result)
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.__helper(candidates, target, 0, 0, [], result)
        return result
