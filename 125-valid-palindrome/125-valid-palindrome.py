class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while r > l:
            while r > l and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
    
    def alphaNum(self, c: chr):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))