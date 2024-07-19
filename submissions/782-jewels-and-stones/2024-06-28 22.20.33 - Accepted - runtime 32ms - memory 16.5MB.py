class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = set(jewels)
        count=0
        for stone in stones:
            if stone in jew:
                count+=1
        return count