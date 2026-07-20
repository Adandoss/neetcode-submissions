class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(c.lower() for c in s if c.isalnum())
        
        left = 0
        right = len(s_clean) - 1

        while left < right:
            if s_clean[left] != s_clean[right]:
                return False
            left += 1
            right -= 1

        return True 
