class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''find highest average
        sliding window approach
        subarray of length k
        find total sum divided by k to get av'''
        total = 0
        average = 0
        curr=0
        
        for i in range(k):
            total+= nums[i]
            curr= total/k
        
        average = curr
        for i in range(k, len(nums)):
            total+= nums[i] - nums[i-k]
            curr = total/k
            average = max(average, curr)
        return average
               