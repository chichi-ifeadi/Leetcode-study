class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        #idea of a set
        #find max element in lsit
        
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        maxi = 0
        for i in counts:
            if i >= maxi and counts[i]==1:
                maxi=i
        if maxi==0:
            return -1
        return maxi