class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=l+1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.remove(nums[r])
            else:
                r+=1
                l+=1
        return len(nums)
        