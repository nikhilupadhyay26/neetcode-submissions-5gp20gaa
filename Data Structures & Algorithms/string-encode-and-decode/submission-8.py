class Solution:
    def encode(self, strs):
        s = ''
        for i in strs:
            s = s+ str(len(i))+'#'+str(i)
        return s

    def decode(self, s: str):
        res = []

        j = 0
        while len(res) < 4:
            length = int(s[j])
            word = s[j+2:j+2+length]
            res.append(word)
            j = j + 2 + length
        return res
