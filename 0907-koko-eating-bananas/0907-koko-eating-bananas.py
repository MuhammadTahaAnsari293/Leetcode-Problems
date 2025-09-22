class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left<=right:
            sum=0
            min_hours=(left+right)//2
            for i in piles:
                pile_hours = (i + min_hours - 1) // min_hours
                sum+=pile_hours
            if sum>h:
                left=min_hours+1
            else:
                right=min_hours-1
        return left
        