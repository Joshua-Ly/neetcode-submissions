class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        sorted_seen = sorted(seen, key=seen.get, reverse = True)
        for num in sorted_seen[:k]:
            res.append(num)
        return res

