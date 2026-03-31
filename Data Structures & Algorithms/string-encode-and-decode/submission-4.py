class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        op = []
        i = 0
        while i == 0:
            hashp = s.find("#")
            word = s[i+hashp+1:int(s[i:hashp])+i+hashp+1]
            print(word)
            s = s[int(s[i:hashp])+i+hashp+1:]
            op.append(word)
            if len(s) == 0:
                i = 1
        return op
