from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res_set = {}
        for word in strs:
            char_set = [0]*26
            for c in word:
                char_set[ord('a')-ord(c)]+=1
            char_set = tuple(char_set)    
            res_set[char_set] = res_set.get(char_set, [])+[word]
        result = []
        for key, words in res_set.items():
            result.append(words)
        return result