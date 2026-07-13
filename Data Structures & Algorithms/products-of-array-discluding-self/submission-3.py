class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zeros_count = 0
        for n in nums: 
            if n != 0: full_product *= n
            else: zeros_count += 1
        
        if zeros_count >= 2: return [0 for _ in nums]

        result = []
        for n in nums:
            if zeros_count == 0:
                result.append(int(full_product/n))
            else:
                if n != 0:
                    result.append(0)
                else:
                    result.append(full_product)

        return result
