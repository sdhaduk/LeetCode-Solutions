class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = [-1]
        max_num = arr[len(arr) - 1]
        
        for i in range(len(arr) - 1):
            max_num = max(arr[len(arr) - 1 - i], max_num)
            new.append(max_num)
            
        new.reverse()
        return new
            
        
        
        
        
        
        
        
        