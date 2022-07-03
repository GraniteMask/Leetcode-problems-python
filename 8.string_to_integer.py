# Brute Method

class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        isNegative = False
        isPositive = False
        for i in s:
            if i == '-':
                if (ord(s[s.index(i)-1]) >= ord('0') and ord(s[s.index(i)-1]) <= ord('9')) and (s.index(i)-1) >= 0:
                    print(s.index(i)-1)
                    return 0
                isNegative = True
            temp = ord(i)
            if i == '+':
                if (ord(s[s.index(i)-1]) >= ord('0') and ord(s[s.index(i)-1]) <= ord('9')) and (s.index(i)-1) >= 0:
                    return 0
                isPositive = True
                continue
            elif temp >= ord('0') and temp <= ord('9'):
                # print(temp)
                result = (result*10) + int(chr(temp))
                print(result)
            elif i == ' ' or i == '-':
                continue
            else:
                break
        if isNegative and not isPositive:
            result = result * (-1)
        elif isNegative and isPositive:
            return 0
        
        print(result)
        
        if result >= (2 ** 31 - 1):
            return (2 ** 31 - 1)
        elif result <= (-2 ** 31):
            return (-2 ** 31)
        else:
            return result

# Optimized

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 : return 0
        st = list(s.strip())
        sign = 1
        
        if len(st):
            sign = -1 if st[0] == '-' else 1
        if len(st):
            if st[0] in ['-','+'] : del st[0]
        ret, i = 0, 0
        while i < len(st) and st[i].isdigit() :
            ret = ret*10 + ord(st[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
    

