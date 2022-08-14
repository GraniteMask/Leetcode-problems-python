class Solution:
    def countSubstrings(self, s: str) -> int:
        global count
        count = 0
        
        def check(l,r):
            global count
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                
                l -= 1
                r += 1
                
        for i in range(len(s)):
            
            check(i, i)
            
            check(i, i+1)
            
        return count
                