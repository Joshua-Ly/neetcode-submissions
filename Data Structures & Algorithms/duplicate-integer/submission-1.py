class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        graph = []
        for i in range(len(nums)):
            if nums[i] in graph:
                return True
            else:
                graph.append(nums[i])
        return False
