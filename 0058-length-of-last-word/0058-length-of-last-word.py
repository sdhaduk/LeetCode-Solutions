class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr, length = len(s) - 1, 0
        
        while s[ptr] == ' ':
            ptr -= 1
        
        while ptr >= 0 and s[ptr] != ' ':
            length += 1
            ptr -= 1
        
        return length
    
            
                
            
            
            
            
            
            
        