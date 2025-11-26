class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i]
            if correct_index == len(nums):
                i+=1
            elif nums[i] != len(nums)+1 and nums[i] != nums[correct_index]:
                nums[correct_index],nums[i] = nums[i], nums[correct_index]
            else:
                i+=1
        i = 0
        while i != len(nums) and nums[i] == i:
            i+=1
        return i