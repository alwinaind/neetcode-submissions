class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_len = len(nums)
        num_set_len = len(set(nums))
        return not (num_len == num_set_len)