class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump_to = 0
        for i in range(len(nums)):
            if can_jump_to < i: break
            can_jump_to = max(i + nums[i], can_jump_to)
            
        return True if can_jump_to >= len(nums) - 1 else False
        
