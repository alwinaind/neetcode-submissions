class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        nums = list(set(nums))
        nums = sorted(nums)
        longest_seq = 1
        i = 0
        print(nums)
        while i < len(nums)-1:
            curr_seq_len = 1
            j = i    
            while nums[j+1]-nums[j] == 1 and j < len(nums)-2:
                curr_seq_len+=1
                j+=1
            if nums[j+1]-nums[j] == 1:
                curr_seq_len+=1
            i = j+1
            if longest_seq < curr_seq_len:
                longest_seq = curr_seq_len
        return longest_seq
            
