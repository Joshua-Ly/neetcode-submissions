class Solution:
    def isPalindrome(self, s: str) -> bool:
        improve = ""
        for char in s:
            if char.isalnum():
                improve += char.lower()
        left = 0
        right = len(improve) - 1
        while right > 0:
            if improve[left] == improve[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
        