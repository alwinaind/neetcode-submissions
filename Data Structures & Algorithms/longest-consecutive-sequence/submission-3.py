class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited= {}
        for i in nums:
            if i-1 in visited:
                visited[i] = True
            else:
                visited[i] = False
        max_count = 1
        curr_key = None
        for key, value in visited.items():
            if not value:
                print(key)
                count=1
                if key+1 in visited:
                    curr_key = key+1
                    count+=1
                    while  curr_key+1 in visited:
                        curr_key+=1
                        count+=1
                    if max_count < count:
                        max_count = count
        return max_count