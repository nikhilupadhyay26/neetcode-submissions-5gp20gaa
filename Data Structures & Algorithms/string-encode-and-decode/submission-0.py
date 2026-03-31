class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + i
        return res

    def decode(self, s: str) -> List[str]:
        op = []
        i = 0
        while i == 0:
            word = s[i+1:int(s[i])+1]
            op.append(word)
            s = s[int(s[i])+1:]
            if len(s) == 0:
                i = 1

        print(op)
        return op
