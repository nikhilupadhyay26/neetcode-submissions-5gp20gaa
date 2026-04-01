class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in nums:
            diff = target - i
            if diff in nums:
                return [nums.index(i), nums.index(diff)]
                break
