class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            
            if sum > target:
                sum -= numbers[r]
                r -= 1
            elif sum < target:
                sum -= numbers[l]
                l += 1
            else:
                return [l+1, r+1]
            
        