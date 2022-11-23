class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0
        
        while s_ptr < len(s):
            if t_ptr == len(t):
                return False
            
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
        
        return True
            
            
            
            
        