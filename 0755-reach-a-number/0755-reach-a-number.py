class Solution:
    def reachNumber(self, target: int) -> int:
        t, m, S = abs(target), 0, 0
        while S < t or (S-t)%2 != 0:
            m+=1
            S+=m
        return m
        