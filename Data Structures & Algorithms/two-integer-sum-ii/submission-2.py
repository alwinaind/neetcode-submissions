class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        val = None
        while val!=target :
            val = numbers[left]+numbers[right]
            if val < target:
                left+=1
            elif val > target:
                right-=1
        return [left+1, right+1]
            