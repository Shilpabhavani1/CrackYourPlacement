class Solution:
    def maxScore(self, s: str) -> int:
        c=0
        i=1
        a=""
        b=""
        while i<len(s):
            a=s[:i].count("0")
            b=s[i:].count("1")
            if a+b>c:
                c=a+b
            i+=1
        # if "0" not in s or "1" not in s:
        #     return len(s)-1
        return c
        
        