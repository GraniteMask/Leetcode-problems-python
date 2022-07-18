# Recursive + Memo

import sys
class Solution:
    
    def superEggDrop(self, k: int, n: int) -> int:
        
        t = [[-1]*(n+1) for i in range(k+1)]
        
        def solve(k,n):
            
            if k == 1:
                return n
            
            if n == 0 or n == 1:
                return n
            
            if t[k][n] != -1:
                return t[k][n]
            
            
            mn = sys.maxsize
            
            for i in range(1,n):
                if t[k-1][i-1] != -1:
                    left = t[k-1][i-1]
                else:
                    left = solve(k-1,i-1)
                    t[k-1][i-1] = left
                
                if t[k][n-i] != -1:
                    right = t[k][n-i] 
                else:
                    right = solve(k,n-i)
                    t[k][n-i] = right
                    
                    
                temp = 1 + max(left, right)
                
                mn = min(mn,temp)
            
            t[k][n] = mn
            
            
            
            return t[k][n]
        
        return solve(k,n)


# Using Binary Search

class Solution:
    """
    Time Complexity: O(k*n* log(n))
    Space Complexity: k*n
    """
    def __init__(self):
        self.t = []
    
    def superEggDrop(self, k: int, n: int) -> int:
        self.t = [[-1 for _ in range(n+1)] for _ in range(k+1)]        
        return self.solve(k,n)
    
    def solve(self,k,n):
        if k == 1 or n == 1 or n == 0:
            return n
        
        # Caching
        if self.t[k][n] != -1:
            return self.t[k][n]
        
        ans = float('inf')
        
        low = 0
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            
            # When the Egg breaks
            left = self.solve(k-1,mid-1)
            
            # When Egg will not break
            right = self.solve(k, n-mid)
            
            # No of moves increase -> 1 + max moves between (left and light)
            temp = 1 + max(left,right)
            
            if left < right:
                low = mid+1
            else:
                high = mid-1
            
            # Find the minimum move
            ans = min(ans,temp)
            
            # Updating the matrix
            self.t[k][n] = ans
        return ans
    
    
    
    
                