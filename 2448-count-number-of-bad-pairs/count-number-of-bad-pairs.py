class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n-1))//2
        hash = {}
        for i in range(n):
            hash[nums[i]-i] = hash.get(nums[i]-i, 0)+1

        for i in hash.values():
            if i > 1:
                total -= (i*(i-1))//2
        return total