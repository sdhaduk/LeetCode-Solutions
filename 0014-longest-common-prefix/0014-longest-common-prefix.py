class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_l = 201
        ptr = 0
        count = 0
        
        for i in range(len(strs)):
            word = strs[i]
            min_l = min(len(word), min_l)
        
        
        while ptr < min_l:
            word = strs[0]
            letter = word[ptr]
            
            for i in range(1,len(strs)):
                tmp_word = strs[i]
                tmp_letter = tmp_word[ptr]
                
                if tmp_letter == letter:
                    count += 1
            
            if count == len(strs)-1:
                prefix += letter
            else:
                return prefix
            
            ptr += 1
            count = 0
        
        return prefix
            
                
                
            
            
            
            
        