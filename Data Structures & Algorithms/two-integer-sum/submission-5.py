class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create the Hashmap
        hash_map = {}
        for index, val in enumerate(nums):
            comp = target - val
            if (comp in hash_map):
                return [hash_map[comp], index]
            hash_map[val] = index