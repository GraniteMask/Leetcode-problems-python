# Using Built in methods

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))