class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = " ".join(filter(lambda x: x.isalnum(), s)).lower()
        return s == s[::-1]