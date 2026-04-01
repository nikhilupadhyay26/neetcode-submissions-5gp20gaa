class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for l1 in t:
            if l1 in s:
                continue
            else:
                return False
        
        return True