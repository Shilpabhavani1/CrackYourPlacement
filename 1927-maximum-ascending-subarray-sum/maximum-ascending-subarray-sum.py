class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums): 
            if not i or nums[i-1] >= nums[i]: val = 0 # reset val 
            val += nums[i]
            ans = max(ans, val)
        return ans 
# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
#         l=[]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 a=nums[i:j+1]
#                 l.append(a)
#         # print(l)
#         m=[]
#         for i in l:
#             if i==sorted(i):
#                 s=set(i)
#                 m.append(sum(s))
#         print(m)
#         return max(m)
        