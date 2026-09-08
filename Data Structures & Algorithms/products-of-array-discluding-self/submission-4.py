class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        prod = nums[0]
        res = []
        if prod == 0:
            zeros.append(0)
        for i in range(1, len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeros.append(i)
        if len(zeros)>1:
            return [0]*len(nums)
        if len(zeros)>0:
            for i in range(len(nums)):
                if i in zeros:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        for i in range(len(nums)):
            res.append(int(prod/nums[i]))
        return res
            