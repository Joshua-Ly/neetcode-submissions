class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                ans.append(seen[complement])
                ans.append(index)
                return ans
            else:
                seen[num] = index