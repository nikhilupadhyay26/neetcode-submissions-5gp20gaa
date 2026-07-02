class Solution:
    def encode(self, strs):
        s = ''
        for i in strs:
            s = s + str(len(i)) + '#' + i
        return s

    def decode(self, s: str):
        res = []

        j = 0
        while j < len(s):

            hash_pos = s.find('#', j)
            length = int(s[j:hash_pos])
            word = s[hash_pos + 1 : hash_pos + 1 + length]
            res.append(word)
            j = hash_pos + 1 + length
        return res
