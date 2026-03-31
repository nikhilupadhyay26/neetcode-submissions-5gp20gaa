class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        
        for c in t:
            if c in set_s:
                continue
            else:
                return False
        return True
        