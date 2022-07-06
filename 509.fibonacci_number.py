class Solution:
    def fib(self, n: int) -> int:
        s = 0
        
        numbers = [0]
        
        if n == 0:
            return 0
            
        
        for i in range(0, n):
                 
            if i == 0:
                s = 1
                numbers.append(s)
            if i >= 1:
                s = numbers[-1] + numbers[len(numbers) - 2]
                numbers.append(s)
                
        return s