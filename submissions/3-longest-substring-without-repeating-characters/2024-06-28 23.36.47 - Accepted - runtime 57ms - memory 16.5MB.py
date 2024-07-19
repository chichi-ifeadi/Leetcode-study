class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        seen = set()
        left=0
        #s = "pwwkew"
        for right in range(len(s)):
            while s[right] in seen:
                
                seen.remove(s[left])
                left+=1
            else:   
                seen.add(s[right])
                maxlen = max(maxlen,right-left+1)
        return maxlen