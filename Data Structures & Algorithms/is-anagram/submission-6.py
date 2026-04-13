class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        fs = {}
        ss = {}

        count = 0
        for i in range(0, len(s)):
            fs[s[i]] = count + 1
            ss[t[i]] = count + 1

        for n in fs:
            if fs[n] == ss.get(n,0):
                continue
            else:
                return False
        return True