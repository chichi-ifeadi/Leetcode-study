class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counts = Counter(text)
        balloon = Counter("balloon")
        
        ans = float("inf")
        for i in balloon:
            ans = min(ans, counts[i]//balloon[i])
        return ans
            