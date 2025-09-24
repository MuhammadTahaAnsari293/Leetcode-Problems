class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            wealth=0
            for j in i:
                wealth+=j
            if max_wealth<wealth:
                max_wealth=wealth
        return max_wealth