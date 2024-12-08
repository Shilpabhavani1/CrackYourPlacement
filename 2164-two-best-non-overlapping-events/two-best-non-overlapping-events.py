class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        time = []
        vals = []
        ans = prefix = 0
        for st, et, val in sorted(events, key=lambda x: x[1]): 
            prefix = max(prefix, val)
            k = bisect_left(time, st)-1
            if k >= 0: val += vals[k]
            ans = max(ans, val)
            time.append(et)
            vals.append(prefix)
        return ans 