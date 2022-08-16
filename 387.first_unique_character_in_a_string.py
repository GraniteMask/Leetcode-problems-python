class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        letters = {}
        
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
                
        for i in s:
            if letters[i] == 1:
                return s.index(i)
            
        return -1