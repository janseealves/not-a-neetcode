class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracked = []
        for num in nums: 
            if num not in tracked: 
                tracked.append(num)
            else: 
                return True
        return False