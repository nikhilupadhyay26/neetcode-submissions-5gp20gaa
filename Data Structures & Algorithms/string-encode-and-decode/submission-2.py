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
            if s[i+1] != "#":
                i = i+1
                word = s[i+2:int(s[0:2])+3]
                s = s[int(s[0:2])+3:]
            else:
                word = s[i+2:int(s[i])+2]
                s = s[int(s[i])+2:]
            op.append(word)
            i = 0
            if len(s) == 0:
                i = 1
        return op
