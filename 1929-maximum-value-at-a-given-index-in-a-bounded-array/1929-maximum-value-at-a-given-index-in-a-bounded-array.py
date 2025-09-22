class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left<=right:
            mid=(left+right)//2
            L, R = index, n-index-1
            if L<=mid-1:
                Left_sum=(L*mid)-(L*(L+1)//2)
            else:
                Left_sum=(mid*(mid-1)//2)+(L-(mid-1))
            if R<=mid-1:
                Right_sum=(R*mid) - (R*(R+1)//2)
            else:
                Right_sum=((mid-1)*mid//2) + (R - (mid-1))
            
            Total = Left_sum+mid+Right_sum
            
            if Total<=maxSum:
                left=mid+1
            else:
                right=mid-1
        return right
        