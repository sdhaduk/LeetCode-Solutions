class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            other_half = target - nums[i]
            if other_half in map:
                return [i, map[other_half]]
            else:
                map[nums[i]] = i
        
            