class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num, val in count.items():
            if val > n / 2:
                return num
            

     
    

    

      