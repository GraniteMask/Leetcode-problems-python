# optimized

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0 or len(haystack) == 0:
            return 0
        
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
                