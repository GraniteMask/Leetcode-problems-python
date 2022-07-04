# Brute Method - Memory Optimized Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in t:
                    s = s.replace(i, "", 1)
                    t = t.replace(t[t.index(i)], "", 1)
            
            if len(s) == 0 and len(t) == 0:
                return True
            else:
                return False

# Time optimized solution - Not good for space complexity and interviews

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)