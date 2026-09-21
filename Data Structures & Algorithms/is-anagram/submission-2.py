class Solution:
    from collections import Counter 
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        w = Counter(t)
        if c == w: 
            return True
        
        return False