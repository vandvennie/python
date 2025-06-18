from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup={}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target- num],i]
            lookup[num]=i

s = Solution()
print(s.twoSum([2,7,11,15],9))