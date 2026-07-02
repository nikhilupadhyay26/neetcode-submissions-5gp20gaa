class Solution:
    def encode(self, strs):
        s = ''
        for i in strs:
            s = s+ str(len(i))+'#'+str(i)
        return s

    def decode(self, s: str):
        res = []
        j = 0
        lentaken = 0
        while lentaken < len(s):
            print('j', j)
            print('s[j]', s[j])
            word = s[j+2:j+2+int(s[j])]
            print(word)
            res.append(word)
            print(res)
            j = int(s[j])+2
            lentaken = len(word) + lentaken + 2
        return res
