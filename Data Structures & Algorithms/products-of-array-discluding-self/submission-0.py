class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        preList = [1]*len(nums)
        for i in range(1, len(nums)):
            preList[i] = nums[i-1] * preList[i-1]
            res[i] = preList[i]

        postList = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            postList[i] = nums[i+1] * postList[i+1]
            res[i] = postList[i] * res[i]
        return res