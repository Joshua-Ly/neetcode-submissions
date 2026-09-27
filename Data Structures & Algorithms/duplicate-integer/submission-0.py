class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = sorted(nums)
        slow = 0
        fast = 1
        while slow < len(l) and fast < len(l):
            if l[slow] == l[fast]:
                return True
            slow += 1
            fast += 1
        return False