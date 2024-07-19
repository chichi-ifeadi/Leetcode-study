class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        
        countm = defaultdict(int)
        
        for i in magazine:
            countm[i]+=1
        
        for r in ransomNote:
            if r not in countm or countm[r]<1:
                return False
            else:
                countm[r]-=1
                
                
        return True