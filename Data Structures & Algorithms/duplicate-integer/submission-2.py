class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        graph = set()
        for i in range(len(nums)):
            if nums[i] in graph:
                return True
            graph.add(nums[i])
        return False
