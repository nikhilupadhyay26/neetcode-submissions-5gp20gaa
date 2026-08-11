class Solution:
    def hasDuplicate(self, nums: List[int]):
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = True
        return False