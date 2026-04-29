class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            leftover = target - num
            if leftover in hashMap:
                return [hashMap[leftover], i]
            hashMap[num] = i