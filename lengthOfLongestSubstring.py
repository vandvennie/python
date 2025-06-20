class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        maxLength = 0
        for right, c in enumerate(s):
            if c in map:
                left = max(left,map[c]+1)
            map[c] = right
            maxLength= max(maxLength,right-left+1)
        return maxLength