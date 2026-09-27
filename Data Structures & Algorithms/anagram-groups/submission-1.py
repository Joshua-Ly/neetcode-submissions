class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for char in strs:
            key = "".join(sorted(char))
            if key in seen:
                seen[key] += [char]
            else:
                seen[key] = [char]
        return list(seen.values())
        
       
            
        