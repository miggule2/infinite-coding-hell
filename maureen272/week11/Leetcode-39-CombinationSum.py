class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        def dfs(index, path, csum):
            if csum > target:
                return
            if csum == target:
                results.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]], csum + candidates[i])
        dfs(0, [], 0)
        return results