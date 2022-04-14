class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            if nums[start] % 2 == 0:
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        return nums
                
                