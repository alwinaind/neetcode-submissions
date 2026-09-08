class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            for c in s:
                encoded_string.append(ord(c))
            encoded_string.append(-1)
        return ','.join([str(x) for x in encoded_string])

    def decode(self, s: str) -> List[str]:
        res = []
        sub_strs = s.split('-1')
        for sub_str in sub_strs[:-1]:
            decoded = ''
            for c in sub_str.split(',')[:-1]:
                if c!='':
                    decoded+=chr(int(c))
            res.append(decoded)
        return res