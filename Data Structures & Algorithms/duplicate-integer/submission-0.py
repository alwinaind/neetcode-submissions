class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         item_hash = []
         for i in nums:
            if i in item_hash:
                return True
            else:
                item_hash.append(i)
         return False