class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join([s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k)])