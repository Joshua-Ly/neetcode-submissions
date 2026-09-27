class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        real = []
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        seen = sorted(result, key=result.get, reverse = True)
        for num in seen[:k]:
            real.append(num)
        return real



        