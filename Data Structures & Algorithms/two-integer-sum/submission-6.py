class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        nums.sort()
        while l< r:
            for i in range(0, len(nums)):
                if nums[l]+nums[r] == target:
                    return [l, r]
                elif nums[l]+nums[r] < target:
                    l = l+1
                elif nums[l]+nums[r] > target:
                    r = r-1
            return [l, r]
            