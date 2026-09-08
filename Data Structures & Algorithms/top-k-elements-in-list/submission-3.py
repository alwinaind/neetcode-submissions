class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        res_dict = {}
        for n in nums:
            res_dict[n] = res_dict.get(n, 0)+1
        top_keys = sorted(res_dict, key=res_dict.get, reverse=True)[:k]
        return top_keys