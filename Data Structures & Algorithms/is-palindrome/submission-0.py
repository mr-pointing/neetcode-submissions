class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''.join(ch for ch in s.lower() if ch.isalnum())
        r2 = reversed(r)
        return r == ''.join(r2)

