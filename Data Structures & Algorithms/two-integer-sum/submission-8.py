class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums=[-1,-2,-3,-4,-5]
        # { -7: 0, -6: 1, -5: 2, ... }

        residuals = defaultdict(int)
        for i, n in enumerate(nums):
            if n in residuals.keys():
                return [residuals[n], i]
            residuals[target - n] = i
        return []



        