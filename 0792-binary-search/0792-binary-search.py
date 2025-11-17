class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        return self.Binarysearch(nums, target, left, right)

    def Binarysearch(self, nums, target, left, right):
        if left>right: # Base Case
            return -1
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.Binarysearch(nums, target, mid+1, right) # recursive call for right subarray
        else:
            return self.Binarysearch(nums, target, left, mid-1) # recursive call for left subarray
        