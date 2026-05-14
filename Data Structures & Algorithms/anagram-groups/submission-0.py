class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            key = "".join(sorted(word))  # or tuple(sorted(word))
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
        return list(hash_map.values())
