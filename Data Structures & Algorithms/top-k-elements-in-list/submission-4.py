class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums: 
            if num in hashMap:
                hashMap[num] = hashMap[num] + 1
                continue
            hashMap[num] = 1
        
        return sorted(hashMap, key=hashMap.get)[::-1][:k]

