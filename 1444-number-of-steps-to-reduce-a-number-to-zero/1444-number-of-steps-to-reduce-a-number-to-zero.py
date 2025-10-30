class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: # base case
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2) # recursive call for even n
        else:
            return 1 + self.numberOfSteps(num - 1) # recursive call for odd n
        