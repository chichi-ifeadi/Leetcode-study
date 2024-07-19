class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #plan is to fins lcnumber in tqo lists
        nums2_set = set(nums2)
        min_num = float("inf")
        curr = False
        for num in nums1:
            if num in nums2_set:
                min_num = min(num, min_num)
                curr= True
            
        if curr is False:
            return -1
        return min_num