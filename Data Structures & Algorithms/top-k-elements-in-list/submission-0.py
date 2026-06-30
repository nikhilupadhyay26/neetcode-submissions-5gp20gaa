class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = {}

        res = [[] for i in range(len(nums)+1)]

        for j in nums:
            count_dic[j] = 1 + count_dic.get(j, 0)
        
        for n, m in count_dic.items():
            res[m].append(n)

        result = []
        for l in range(len(res)-1, 0, -1):
            for t in res[l]:
                result.append(t)
                if len(result) == k:
                    return result
