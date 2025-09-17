class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        left = 1
        right = target
        while left < right:
            min_steps = left + (right - left) // 2
            if min_steps * (min_steps + 1) // 2 >= target:
                right = min_steps
            else:
                left = min_steps + 1
        min_steps = left

        diff = min_steps * (min_steps + 1) // 2 - target
        if diff % 2:
            min_steps += min_steps % 2 + 1
        return min_steps

        