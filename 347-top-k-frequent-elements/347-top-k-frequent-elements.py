class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq =[[] for i in range(len(nums) + 1)] 
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key in count:
            freq[count[key]].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for value in freq[i]:
                res.append(value)
                if len(res) == k:
                    return res
            
            
            
        
        
        
        
            
        
        
            
            
                
                
                
                
            
        