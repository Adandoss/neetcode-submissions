class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zeros_count = 0
        for n in nums: 
            if n != 0: full_product *= n
            else: zeros_count += 1
        
        if zeros_count >= 2:    return [0 for _ in nums]
        elif zeros_count == 1:  return [0 if n != 0 else full_product for n in nums]
        else:                   return [int(full_product/n) for n in nums]

