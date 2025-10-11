class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left<right:
            add = 0
            piece = 1
            mid=left+(right-left)//2
            for num in nums:
                add+=num
                if add > mid:
                    add = num
                    piece+=1
            if piece <= k:
                right = mid
            else:
                left = mid+1
        return left
        