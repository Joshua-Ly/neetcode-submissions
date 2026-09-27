class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        sorted_nums = sorted(seen, key=seen.get, reverse = True)
        for num in sorted_nums[:k]:
            result.append(num)
            
        return result
