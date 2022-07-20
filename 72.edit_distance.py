# Optimized - Top-Down DP 2D array

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        
        if n == 0 and m == 0:
            return 0
        
        if word1 == word2:
            return 0
        
        t = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    t[i][j] = j
                if j == 0:
                    t[i][j] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1]
                    
                else:
                    t[i][j] = 1 + min(t[i-1][j], t[i][j-1], t[i-1][j-1])
        
        return t[-1][-1]