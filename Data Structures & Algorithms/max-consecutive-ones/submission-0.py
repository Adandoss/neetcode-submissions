class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count: int=0
        max_consecutives: int=0

        for n in nums:
            if n==1: 
                ones_count += 1
                if ones_count > max_consecutives: 
                    max_consecutives += 1 
            else:
                ones_count = 0
        
        return max_consecutives