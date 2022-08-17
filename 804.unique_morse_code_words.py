class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        
        for i in words:
            temp = ""
            for j in i:
                temp += table[ord(j) - ord('a')]
            res.add(temp)
            
        return len(res)