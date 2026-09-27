class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        for i in range(len(numbers)):
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            elif res < target:
                left += 1
            else:
                right -= 1
      
        