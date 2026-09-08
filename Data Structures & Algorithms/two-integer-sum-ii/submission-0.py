class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        while l < r:
            if target - numbers[l] == numbers[r]:
                return [l+1, r+1]
            else:
                 r-=1
                 if r == l:
                    r = len(numbers) -1
                    l+=1