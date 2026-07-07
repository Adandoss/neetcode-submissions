class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = defaultdict(int)
        for n in nums:
            if n in num_counts: 
                return True
            num_counts[n] += 1

        return False            
        

