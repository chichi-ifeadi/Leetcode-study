class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''find highest average
        sliding window approach
        subarray of length k
        find total sum divided by k to get av'''
        total = 0
        
        curr=0
        
        for i in range(k):
            curr+= nums[i]
        total =curr
        
        average = curr
        for i in range(k, len(nums)):
            curr+= nums[i] - nums[i-k]
            
            total = max(total, curr)
        return total/k
               