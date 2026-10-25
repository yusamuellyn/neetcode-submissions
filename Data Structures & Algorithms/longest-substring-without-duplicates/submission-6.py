class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        temp = 0
        left = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= left:
                left = seen[s[i]] + 1
            seen[s[i]] = i
            temp = i - left + 1
 
            if temp > longest:
                longest = temp
        return longest
            





