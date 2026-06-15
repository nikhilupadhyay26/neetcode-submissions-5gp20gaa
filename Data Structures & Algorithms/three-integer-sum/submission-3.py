class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i]

            l = i+1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + target == 0:
                    res.append([target, nums[l], nums[r]])
                    l = l+1 
                    while nums[l] == nums[l-1] and l < r:
                        l = l+1
                elif nums[l] + nums[r] + target < 0:
                    l = l+1
                elif nums[l] + nums[r] + target > 0:
                    r = r-1
        return res