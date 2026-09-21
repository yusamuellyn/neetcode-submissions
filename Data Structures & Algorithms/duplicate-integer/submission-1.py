class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for s in nums:
            if s in seen: 
                return True
            else:
                seen.add(s)
        return False