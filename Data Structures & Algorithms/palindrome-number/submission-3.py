class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_string = str(x)
        i, j = 0, len(x_string) - 1

        while(i < j):
            if x_string[i] != x_string[j]:
                return False
            i += 1
            j -= 1
            
        return True
