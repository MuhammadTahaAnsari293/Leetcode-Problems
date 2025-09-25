class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if letters[mid] > target:
                right = mid - 1         # search left for smaller > target
            else:
                left = mid + 1          # need bigger character
        return letters[left%len(letters)] # 3%3=0