class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = sorted(s)
        td = sorted(t)
        if sd == td:
            return True
        return False        