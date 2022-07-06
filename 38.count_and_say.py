class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return '1'

        def helper(s):
            ans = ""
            length = len(s)
			
            temp = 1
            for i in range(length):
				
                if i <= (length - 2) and s[i] == s[i+1]:
                    temp += 1
				
                else:
                    ans += str(temp) + str(s[i])
                    temp = 1
            return ans
			
		
        curr = "1"
        for i in range(1, n):
            curr = helper(curr)
        return curr
                    
        
        
        
        