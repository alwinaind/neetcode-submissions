class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0)+1
        
        for c in t:
            t_map[c] = t_map.get(c, 0)+1
        
        print(s_map)
        print(t_map)
        for k in s_map.keys():
            if s_map[k] != t_map.get(k, 0):
                return False
        return True
