class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tsum=sum(nums)
        psum=0
        c=0
        for i in range(len(nums)-1):
            psum+=nums[i]
            if psum>=(tsum-psum):
                c+=1
        return c