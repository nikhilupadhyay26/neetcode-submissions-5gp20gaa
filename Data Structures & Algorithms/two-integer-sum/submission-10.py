class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thash = {}

        for i in nums:
            if target - i in thash:
                return [nums.index(target- i), nums.index(i)]
            thash[i] = i

            