class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        #idea of a set
        #find max element in lsit
        
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0)+1
            
        maxi = 0
        for i in seen:
            if i >= maxi and seen[i]==1:
                maxi=i
        if maxi==0:
            return -1
        return maxi