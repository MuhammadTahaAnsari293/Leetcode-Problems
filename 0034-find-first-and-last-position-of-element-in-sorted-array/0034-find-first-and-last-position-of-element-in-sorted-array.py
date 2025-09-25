class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        idx = -1
        # 1st occurance
        left, right = 0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                right=mid-1
                idx=mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        res.append(idx)
        
        # last occurance
        left, right = 0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                left=mid+1
                idx=mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        res.append(idx)
        
        return res
        