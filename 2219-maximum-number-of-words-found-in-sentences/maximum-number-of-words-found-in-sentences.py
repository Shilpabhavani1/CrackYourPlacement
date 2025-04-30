class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        for i in range(len(sentences)):
            s=sentences[i]
            temp=1
            for j in range(len(s)):
                a=s[j]
                if a==" ":
                    temp+=1
            c=max(c,temp)         
        return c
        