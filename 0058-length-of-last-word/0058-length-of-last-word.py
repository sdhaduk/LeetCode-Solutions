class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = 0
        
        while ptr < len(s):
            if s[ptr] != ' ':
                count = 0
                while ptr < len(s) and s[ptr] != ' ':
                    count += 1
                    ptr += 1
            
            ptr += 1
            
        return count
                
            
                
            
            
            
            
            
            
        