class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)
        while left < right: 
            if not s[left].isalnum():
                left = left + 1
                continue
            if not s[right - 1].isalnum():
                right = right - 1
                continue

            if s[left].lower() == s[right - 1].lower():
                left += 1
                right = right - 1
            else:
                return False

        return True