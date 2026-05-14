class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # Initialise empty the dictionary

        for index, number in enumerate(nums): # Fill dictionary 
            hash_map[number] = index

        for index, number in enumerate(nums):
            number_to_find = target - number
            if (number_to_find in hash_map and index != hash_map[number_to_find]):
                return [index, hash_map[number_to_find]]


        
        