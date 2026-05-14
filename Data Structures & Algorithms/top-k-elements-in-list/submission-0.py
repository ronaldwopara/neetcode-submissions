class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        res = []
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        sorted_values = sorted(hash_map.values(), reverse=True)[:k]
        for num in hash_map.keys():
            if (hash_map[num] in sorted_values) and (num not in res):
                res.append(num)
        return res