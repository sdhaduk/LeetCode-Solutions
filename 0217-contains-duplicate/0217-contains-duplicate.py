class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            if n in map:
                return True
            else:
                map[n] = 1
        return False