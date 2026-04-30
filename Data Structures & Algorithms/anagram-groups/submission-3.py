class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs: 
            sorted_str = ''.join([char for char in sorted(s)])
            if sorted_str in hashMap:
                hashMap[sorted_str].append(s)
            else: 
                hashMap[sorted_str] = [s]    
        return list(hashMap.values())