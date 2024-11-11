class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in d:
                return d[diff],i
            d[n]=i
        # d={}
        # for i,n in enumerate(nums):
        #     diff=target-n
        #     if diff in d:
        #         return d[diff],i
        #     d[n]=i
        # return
        # prevmap={} #hash map val:ind
        # for i,n in enumerate(nums):
        #     diff=target-n
        #     if diff in prevmap:
        #         return prevmap[diff],i
        #     prevmap[n]=i
        # return
        # for i in range(len(nums)+1):
        #     if nums[i]+nums[i+1]==target:
        #         return i,i+1
        