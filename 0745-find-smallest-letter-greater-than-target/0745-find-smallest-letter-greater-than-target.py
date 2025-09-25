class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        result = letters[0]  # default wrap-around
    
        while left <= right:
            mid = left + (right-left) // 2
            if letters[mid] > target:
                result = letters[mid]   # possible candidate
                right = mid - 1         # search left for smaller > target
            else:
                left = mid + 1          # need bigger character
        return result