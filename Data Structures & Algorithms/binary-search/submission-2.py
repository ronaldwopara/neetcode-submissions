class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = (low + high)//2

            check = nums[mid]
            if target == check:
                return mid
            elif target > check:
                low = mid + 1
            elif target < check:
                high = mid - 1
            
        return -1
