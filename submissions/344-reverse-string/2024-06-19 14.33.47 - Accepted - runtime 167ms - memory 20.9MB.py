class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r=len(s)-1
        val = ""
        while l<r:
            val= s[l]
            s[l]= s[r]
            s[r] = val
            l+=1
            r-=1