class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(ch: str) -> bool:
            return ch in {'a', 'e', 'i', 'o', 'u'}

        valid = [1 if is_vowel(word[0]) and is_vowel(word[-1]) else 0 for word in words]

        prefix = [0] * len(valid)
        prefix[0] = valid[0]
        for i in range(1, len(valid)):
            prefix[i] = prefix[i - 1] + valid[i]

        result = []
        for li, ri in queries:
            if li == 0:
                result.append(prefix[ri])
            else:
                result.append(prefix[ri] - prefix[li - 1])

        return result
