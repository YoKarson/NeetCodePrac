from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        
        return l
    
nums = [1, 2, 3, 4, 5]
sol = Solution()

print(sol.removeElement(nums, 2))
print(nums)