class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(length, peak):
            if length<=peak-1:
                return ((length*peak)-(length*(length+1)//2))
            else:
                return ((peak*(peak-1)//2)+(length-(peak-1)))

        left, right = 1, maxSum
        while left<=right:
            mid=(left+right)//2
            Total=side_sum(index,mid)+mid+side_sum(n-1-index,mid)
            if Total<=maxSum:
                left=mid+1
            else:
                right=mid-1
        return right
        