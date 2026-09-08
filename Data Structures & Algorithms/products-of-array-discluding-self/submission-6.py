class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                product*=nums[i]
        if not zero_index:
            return [int(product/n) for n in nums]
        else:
            print(zero_index)
            result = [0]*len(nums)
            if len(zero_index) == 1:
                result[zero_index[0]] = product
            return result