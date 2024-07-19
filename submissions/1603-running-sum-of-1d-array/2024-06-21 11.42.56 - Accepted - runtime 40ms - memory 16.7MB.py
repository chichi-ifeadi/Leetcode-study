class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''idea of prefix sum
        should i use a new array
        loop through the array'''
        prefix = [nums[0]]
        
        for index in range(1,len(nums)):
            prefix.append(nums[index] + prefix[-1])
        return prefix
            