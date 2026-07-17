class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence_length = 0
        current_sequence_length = 0        
        for n in nums:
            current_sequence_length = 0 

            if n in nums_set:
                nums_set.remove(n)
                current_sequence_length += 1  
            else: continue 

            left = n-1  
            right = n+1

            while True:
                if left in nums_set:
                    nums_set.remove(left)
                    current_sequence_length += 1  
                    left -= 1
                else: break 

            while True:
                if right in nums_set:
                    nums_set.remove(right)
                    current_sequence_length += 1  
                    right += 1
                else: break
            
            if current_sequence_length > max_sequence_length: 
                max_sequence_length = current_sequence_length
        
        return max_sequence_length

            
                