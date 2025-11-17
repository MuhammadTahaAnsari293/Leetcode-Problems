class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 ==0: # checks till the number even
            n = n // 2
        return n == 1
        