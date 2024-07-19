class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #find len of nums
        
        for i in range(len(nums)+1):
            #check if num is in nums
            if i not in nums:
                return i
        return