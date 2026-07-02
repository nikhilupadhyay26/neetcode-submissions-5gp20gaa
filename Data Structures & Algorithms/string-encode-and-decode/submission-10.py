class Solution:
    def encode(self, strs):
        s = ''
        for i in strs:
            s = s+ str(len(i))+'#'+str(i)
        return s

    def decode(self, s: str):
        res = []

        j = 0
        while j < len(s):
            print('j', j)
            hash_pos = s.find('#', j)
            length = int(s[j:hash_pos])
            print('length', length)
            word = s[j+2:j+2+length]
            print('word', word)
            res.append(word)
            print('res', res)
            j = j + 2 + length
        return res
