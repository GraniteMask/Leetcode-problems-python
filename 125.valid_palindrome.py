class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ""
        
        for i in s:
            asciiVal = ord(i)
            if (asciiVal >= 65 and asciiVal <= 90) or (asciiVal >= 97 and asciiVal <= 122) or (asciiVal >= 48 and asciiVal <= 57):
                string += i
                
        string = string.lower()
        
        if string == string[::-1]:
            return True
        else:
            return False
            
                