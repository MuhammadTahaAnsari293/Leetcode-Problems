class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_max=0
        for i in nums:
            count = 0
            while i>0:
                i = i//10
                count+=1
            if count%2 ==0:
                count_max+=1
        return count_max