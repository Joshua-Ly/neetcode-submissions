class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        best = 0
        for num in sett:
            if num - 1 not in sett:
                length = 1
                while (num + length) in sett:
                #used as condition variable and counter
                    length += 1
                best = max(best, length)
        return best


           
    
    
    
        
        