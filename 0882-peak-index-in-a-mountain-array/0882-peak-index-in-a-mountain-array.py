class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left<right:
            mid = left + (right-left)//2
            if arr[mid]>arr[mid+1]:
                right=mid # this may be the answer that's why right!=mid-1
            else:
                left=mid+1 # mid has been already checked
        return left