class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for c in t:
            if c in s:
                continue
            else:
                return False
        return True
        