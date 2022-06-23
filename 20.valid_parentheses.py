class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = { ")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in table:
                if stack and stack[-1] == table[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False