class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
                
            if nums[k] > 0:
                break

            i, j = k + 1, len(nums) - 1
            
            while i < j:
                three_sum = nums[k] + nums[i] + nums[j]
                
                if three_sum == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                        
                elif three_sum < 0:
                    i += 1
                else:
                    j -= 1
                    
        return result