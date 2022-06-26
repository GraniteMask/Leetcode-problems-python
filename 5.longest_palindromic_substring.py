class Solution:
    def longestPalindrome(self, s: str) -> str:
        global res 
        res = ""
        global resLen 
        resLen = 0
        
        def check(l,r):
            global resLen
            global res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            
            # checking odd length palindrome
            
            check(i,i)
            
            # checking even length palindrome
            
            check(i,i+1)
            
        return res
            
            