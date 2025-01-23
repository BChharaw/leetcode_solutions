#Problem No. 217
import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in range(len(nums)):
            if nums[i] in mem:
                return True
            mem.add(nums[i])
            
        return False
